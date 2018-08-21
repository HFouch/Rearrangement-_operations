if __name__ == "__main__":

    filename = 'GenomeB_names_positions_TEST'


    from class_defining_edge_series import EdgeSeriesAndSequenceBlocks
    from class_find_operation_sets import IdentificationOfOperationSets


    generate_list_of_sequence_blocks = EdgeSeriesAndSequenceBlocks()
    sequence_blocks = generate_list_of_sequence_blocks.ListSequenceBlocks(filename)

    find_operations_sets = IdentificationOfOperationSets()
    Operation_sets = find_operations_sets.find_operation_sets(sequence_blocks)
    