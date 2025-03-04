old_df, new_df = test_data
    dp = DataPuller(old_df, new_df)

    full_address = dp.create_full_address(old_df)
    expected = pd.Series(['123 Main St, New York, 10001', '456 Oak St, Los Angeles, 90001'])

    pd.testing.assert_series_equal(full_address, expected)

def test_get_new_addresses(test_data):
    """Tests if new addresses are identified correctly."""
    old_df, new_df = test_data
    dp = DataPuller(old_df, new_df)
    new_only_df = dp.get_new_addresses()

    # Expected new address
    expected_df = pd.DataFrame({
        'address': ['789 Pine St'],
        'city': ['San Francisco'],
        'zip': ['94101'],
        'as_of_date': ['2024-02-02'],
        'full_address': ['789 Pine St, San Francisco, 94101']
    })

    pd.testing.assert_frame_equal(new_only_df.reset_index(drop=True), expected_df)

def test_performance():
    """Tests if function runs efficiently on large data."""
    num_records = 1_000_000  # 1 million rows for testing

    old_df = pd.DataFrame({
        'address': ['123 Main St'] * num_records,
        'city': ['New York'] * num_records,
        'zip': ['10001'] * num_records,
        'as_of_date': ['2024-01-01'] * num_records
    })

    new_df = pd.DataFrame({
        'address': ['456 Oak St'] * num_records,
        'city': ['Los Angeles'] * num_records,
        'zip': ['90001'] * num_records,
        'as_of_date': ['2024-02-01'] * num_records
    })

    dp = DataPuller(old_df, new_df)

    import time
    start_time = time.time()
    new_only_df = dp.get_new_addresses()
    end_time = time.time()

    # Ensure at least 1 new record is detected
    assert not new_only_df.empty

    # Check if function runs in under 2 seconds for 1M rows
    assert (end_time - start_time) < 2.0, "Performance test failed


