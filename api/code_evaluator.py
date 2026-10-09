import time
import sys
import io
import ast
import traceback
import math
import subprocess
import json
import sqlite3

def evaluate_code(submitted_code, test_cases, language='python'):
    """
    Evaluates code in Python, JavaScript (via Node.js), or SQL (via SQLite in-memory).
    """
    language = language.lower()
    
    if language == 'javascript' or language == 'js':
        return evaluate_javascript_code(submitted_code, test_cases)
    elif language == 'sql':
        return evaluate_sql_code(submitted_code, test_cases)
    else:
        return evaluate_python_code(submitted_code, test_cases)


def evaluate_python_code(submitted_code, test_cases):
    start_time = time.time()
    results = []
    all_passed = True

    try:
        compiled_code = compile(submitted_code, '<user_code>', 'exec')
    except Exception as syntax_err:
        return {
            'status': 'Syntax Error',
            'passed_count': 0,
            'total_tests': len(test_cases),
            'execution_time_ms': 0.0,
            'error_message': f"SyntaxError: {str(syntax_err)}",
            'results': []
        }

    exec_globals = {
        'math': math,
        'abs': abs, 'len': len, 'range': range, 'sorted': sorted,
        'min': min, 'max': max, 'sum': sum, 'enumerate': enumerate,
        'zip': zip, 'map': map, 'filter': filter, 'list': list,
        'dict': dict, 'set': set, 'str': str, 'int': int, 'float': float,
        'bool': bool, 'True': True, 'False': False, 'None': None
    }

    try:
        exec(compiled_code, exec_globals)
    except Exception as exec_err:
        return {
            'status': 'Runtime Error',
            'passed_count': 0,
            'total_tests': len(test_cases),
            'execution_time_ms': round((time.time() - start_time) * 1000, 2),
            'error_message': traceback.format_exc(limit=2),
            'results': []
        }

    passed_count = 0
    for idx, test_case in enumerate(test_cases):
        test_input_str = test_case.get('input', '()')
        expected_output_str = test_case.get('expected_output', '').strip()

        try:
            test_args = eval(test_input_str, exec_globals)
            if not isinstance(test_args, tuple):
                test_args = (test_args,)

            user_funcs = [v for k, v in exec_globals.items() if callable(v) and k not in ['math', 'abs', 'len', 'range', 'sorted', 'min', 'max', 'sum', 'enumerate', 'zip', 'map', 'filter', 'list', 'dict', 'set', 'str', 'int', 'float', 'bool']]

            if not user_funcs:
                raise ValueError("No function defined in Python code!")

            target_fn = user_funcs[-1]
            actual_res = target_fn(*test_args)
            actual_output_str = repr(actual_res)

            expected_res = eval(expected_output_str, exec_globals) if expected_output_str else None
            is_passed = (actual_res == expected_res) or (actual_output_str == expected_output_str)

            if is_passed:
                passed_count += 1
            else:
                all_passed = False

            results.append({
                'test_num': idx + 1,
                'input': test_input_str,
                'expected': expected_output_str,
                'actual': actual_output_str,
                'passed': is_passed
            })
        except Exception as tc_err:
            all_passed = False
            results.append({
                'test_num': idx + 1,
                'input': test_input_str,
                'expected': expected_output_str,
                'actual': f"Error: {str(tc_err)}",
                'passed': False
            })

    execution_time_ms = round((time.time() - start_time) * 1000, 2)
    final_status = 'Accepted' if (all_passed and passed_count == len(test_cases)) else 'Wrong Answer'

    return {
        'status': final_status,
        'passed_count': passed_count,
        'total_tests': len(test_cases),
        'execution_time_ms': execution_time_ms,
        'error_message': None,
        'results': results
    }


def evaluate_javascript_code(submitted_code, test_cases):
    start_time = time.time()
    results = []
    all_passed = True
    passed_count = 0

    # Wrapper script for Node.js
    runner_script = f"""
{submitted_code}

const testCases = {json.dumps(test_cases)};
const results = [];
let passedCount = 0;

// Find exported or last defined function
let targetFn = null;
if (typeof twoSum === 'function') targetFn = twoSum;
else if (typeof reverseString === 'function') targetFn = reverseString;
else if (typeof findMax === 'function') targetFn = findMax;
else if (typeof isPalindrome === 'function') targetFn = isPalindrome;

for (let i = 0; i < testCases.length; i++) {{
    const tc = testCases[i];
    try {{
        const args = eval('[' + tc.input.replace(/^\\(/, '').replace(/\\)$/, '') + ']');
        let actual = undefined;
        if (targetFn) {{
            actual = targetFn(...args);
        }}
        const expected = eval(tc.expected_output);
        const isPassed = JSON.stringify(actual) === JSON.stringify(expected) || String(actual) === String(tc.expected_output).replace(/^'|'$/g, '');
        if (isPassed) passedCount++;
        results.push({{
            test_num: i + 1,
            input: tc.input,
            expected: tc.expected_output,
            actual: JSON.stringify(actual),
            passed: isPassed
        }});
    }} catch (err) {{
        results.push({{
            test_num: i + 1,
            input: tc.input,
            expected: tc.expected_output,
            actual: 'Error: ' + err.message,
            passed: false
        }});
    }}
}}

console.log(JSON.stringify({{ passed_count: passedCount, results: results }}));
"""

    try:
        proc = subprocess.run(
            ['node', '-e', runner_script],
            capture_output=True,
            text=True,
            timeout=3
        )
        if proc.returncode != 0:
            return {
                'status': 'Runtime Error',
                'passed_count': 0,
                'total_tests': len(test_cases),
                'execution_time_ms': round((time.time() - start_time) * 1000, 2),
                'error_message': proc.stderr or 'Node.js execution error',
                'results': []
            }

        output_data = json.loads(proc.stdout.strip())
        passed_count = output_data['passed_count']
        results = output_data['results']
        all_passed = (passed_count == len(test_cases))

    except Exception as err:
        return {
            'status': 'Runtime Error',
            'passed_count': 0,
            'total_tests': len(test_cases),
            'execution_time_ms': round((time.time() - start_time) * 1000, 2),
            'error_message': str(err),
            'results': []
        }

    return {
        'status': 'Accepted' if all_passed else 'Wrong Answer',
        'passed_count': passed_count,
        'total_tests': len(test_cases),
        'execution_time_ms': round((time.time() - start_time) * 1000, 2),
        'error_message': None,
        'results': results
    }


def evaluate_sql_code(submitted_code, test_cases):
    start_time = time.time()
    try:
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE users (id INT, name TEXT, age INT);")
        cursor.execute("INSERT INTO users VALUES (1, 'Alice', 25), (2, 'Bob', 30), (3, 'Charlie', 35);")
        conn.commit()

        cursor.execute(submitted_code)
        rows = cursor.fetchall()
        actual_output = str(rows)

        passed = len(rows) > 0
        return {
            'status': 'Accepted' if passed else 'Wrong Answer',
            'passed_count': 1 if passed else 0,
            'total_tests': 1,
            'execution_time_ms': round((time.time() - start_time) * 1000, 2),
            'error_message': None,
            'results': [{
                'test_num': 1,
                'input': 'SELECT * FROM users;',
                'expected': 'Query Results Returned',
                'actual': actual_output,
                'passed': passed
            }]
        }
    except Exception as err:
        return {
            'status': 'SQL Error',
            'passed_count': 0,
            'total_tests': 1,
            'execution_time_ms': round((time.time() - start_time) * 1000, 2),
            'error_message': f"SQLite Error: {str(err)}",
            'results': []
        }
