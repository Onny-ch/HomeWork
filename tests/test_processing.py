from src.processing import filter_by_state, sort_by_date
import pytest


def test_filter_by_state_execution(account_transaction_data):
    assert (filter_by_state(account_transaction_data, "EXECUTION") ==
            [elem for elem in account_transaction_data if elem["state"] == "EXECUTION"])


def test_filter_by_state_canceled(account_transaction_data):
    assert (filter_by_state(account_transaction_data, "CANCELED") ==
            [elem for elem in account_transaction_data if elem["state"] == "CANCELED"])


def test_sort_by_date_reverse(account_transaction_data):
    assert (sort_by_date(account_transaction_data, True) ==
            sorted(account_transaction_data, key=lambda transact_data_dict: transact_data_dict['date'], reverse=True))


def test_sort_by_date_not_reverse(account_transaction_data):
    assert (sort_by_date(account_transaction_data, False) ==
            sorted(account_transaction_data, key=lambda transact_data_dict: transact_data_dict['date'], reverse=False))
