import pytest
from capital_gain import Operation, OperationTax, process_operations


@pytest.mark.parametrize("operations, expected", [
    # Caso 1
    (
        [
            Operation(**{"operation": "buy", "unit-cost": 10.00, "quantity": 100}),
            Operation(**{"operation": "sell", "unit-cost": 15.00, "quantity": 50}),
            Operation(**{"operation": "sell", "unit-cost": 15.00, "quantity": 50}),
        ],
        [
            OperationTax(tax=0.0),
            OperationTax(tax=0.0),
            OperationTax(tax=0.0),
        ],
    ),
    # Caso 2
    (
        [
            Operation(**{"operation": "buy", "unit-cost": 10.00, "quantity": 10000}),
            Operation(**{"operation": "sell", "unit-cost": 20.00, "quantity": 5000}),
            Operation(**{"operation": "sell", "unit-cost": 5.00, "quantity": 5000}),
        ],
        [
            OperationTax(tax=0.0),
            OperationTax(tax=10000.0),
            OperationTax(tax=0.0),
        ],
    ),
    # Caso 3
    (
        [
            Operation(**{"operation": "buy", "unit-cost": 10.00, "quantity": 10000}),
            Operation(**{"operation": "sell", "unit-cost": 5.00, "quantity": 5000}),
            Operation(**{"operation": "sell", "unit-cost": 20.00, "quantity": 3000}),
        ],
        [
            OperationTax(tax=0.0),
            OperationTax(tax=0.0),
            OperationTax(tax=1000.0),
        ],
    ),
    # Caso 4
    (
        [
            Operation(**{"operation": "buy", "unit-cost": 10.00, "quantity": 10000}),
            Operation(**{"operation": "buy", "unit-cost": 25.00, "quantity": 5000}),
            Operation(**{"operation": "sell", "unit-cost": 15.00, "quantity": 10000}),
        ],
        [
            OperationTax(tax=0.0),
            OperationTax(tax=0.0),
            OperationTax(tax=0.0),
        ],
    ),
    # Caso 5
    (
        [
            Operation(**{"operation": "buy", "unit-cost": 10.00, "quantity": 10000}),
            Operation(**{"operation": "buy", "unit-cost": 25.00, "quantity": 5000}),
            Operation(**{"operation": "sell", "unit-cost": 15.00, "quantity": 10000}),
            Operation(**{"operation": "sell", "unit-cost": 25.00, "quantity": 5000}),
        ],
        [
            OperationTax(tax=0.0),
            OperationTax(tax=0.0),
            OperationTax(tax=0.0),
            OperationTax(tax=10000.0),
        ],
    ),
    # Caso 6
    (
        [
            Operation(**{"operation": "buy", "unit-cost": 10.00, "quantity": 10000}),
            Operation(**{"operation": "sell", "unit-cost": 2.00, "quantity": 5000}),
            Operation(**{"operation": "sell", "unit-cost": 20.00, "quantity": 2000}),
            Operation(**{"operation": "sell", "unit-cost": 20.00, "quantity": 2000}),
            Operation(**{"operation": "sell", "unit-cost": 25.00, "quantity": 1000}),
        ],
        [
            OperationTax(tax=0.0),
            OperationTax(tax=0.0),
            OperationTax(tax=0.0),
            OperationTax(tax=0.0),
            OperationTax(tax=3000.0),
        ],
    ),
    # Caso 7
    (
        [
            Operation(**{"operation": "buy", "unit-cost": 10.00, "quantity": 10000}),
            Operation(**{"operation": "sell", "unit-cost": 2.00, "quantity": 5000}),
            Operation(**{"operation": "sell", "unit-cost": 20.00, "quantity": 2000}),
            Operation(**{"operation": "sell", "unit-cost": 20.00, "quantity": 2000}),
            Operation(**{"operation": "sell", "unit-cost": 25.00, "quantity": 1000}),
            Operation(**{"operation": "buy", "unit-cost": 20.00, "quantity": 10000}),
            Operation(**{"operation": "sell", "unit-cost": 15.00, "quantity": 5000}),
            Operation(**{"operation": "sell", "unit-cost": 30.00, "quantity": 4350}),
            Operation(**{"operation": "sell", "unit-cost": 30.00, "quantity": 650}),
        ],
        [
            OperationTax(tax=0.0),
            OperationTax(tax=0.0),
            OperationTax(tax=0.0),
            OperationTax(tax=0.0),
            OperationTax(tax=3000.0),
            OperationTax(tax=0.0),
            OperationTax(tax=0.0),
            OperationTax(tax=3700.0),
            OperationTax(tax=0.0),
        ],
    ),
    # Caso 8
    (
        [
            Operation(**{"operation": "buy", "unit-cost": 10.00, "quantity": 10000}),
            Operation(**{"operation": "sell", "unit-cost": 50.00, "quantity": 10000}),
            Operation(**{"operation": "buy", "unit-cost": 20.00, "quantity": 10000}),
            Operation(**{"operation": "sell", "unit-cost": 50.00, "quantity": 10000}),
        ],
        [
            OperationTax(tax=0.0),
            OperationTax(tax=80000.0),
            OperationTax(tax=0.0),
            OperationTax(tax=60000.0),
        ],
    ),
    # Caso 9
    (
        [
            Operation(**{"operation": "buy", "unit-cost": 5000.00, "quantity": 10}),
            Operation(**{"operation": "sell", "unit-cost": 4000.00, "quantity": 5}),
            Operation(**{"operation": "buy", "unit-cost": 15000.00, "quantity": 5}),
            Operation(**{"operation": "buy", "unit-cost": 4000.00, "quantity": 2}),
            Operation(**{"operation": "buy", "unit-cost": 23000.00, "quantity": 2}),
            Operation(**{"operation": "sell", "unit-cost": 20000.00, "quantity": 1}),
            Operation(**{"operation": "sell", "unit-cost": 12000.00, "quantity": 10}),
            Operation(**{"operation": "sell", "unit-cost": 15000.00, "quantity": 3}),
        ],
        [
            OperationTax(tax=0.0),
            OperationTax(tax=0.0),
            OperationTax(tax=0.0),
            OperationTax(tax=0.0),
            OperationTax(tax=0.0),
            OperationTax(tax=0.0),
            OperationTax(tax=1000.0),
            OperationTax(tax=2400.0),
        ],
    ),
])
def test_process_operations_with_parametrization(operations, expected):
    results = process_operations(operations)
    assert results == expected
