if __name__ == "__main__":

    filename = 'GenomeB_names_positions'

    from class_defining_edge_series import EdgeSeriesAndSequenceBlocks
    from class_defining_rearrangment_operations import RearrangementOperationIdentification
    from class_defining_COI_lists import IdentifyIncompatibleOperations

    generate_list_of_sequence_blocks = EdgeSeriesAndSequenceBlocks()
    sequence_blocks = generate_list_of_sequence_blocks.ListSequenceBlocks(filename)

    generate_the_series_of_edges = EdgeSeriesAndSequenceBlocks()
    edge_series = generate_the_series_of_edges.GenerateEdgesSeries(sequence_blocks)

    print(sequence_blocks)
    find_rearrangement_operations = RearrangementOperationIdentification()
    Inversions = find_rearrangement_operations.InversionIdentification(edge_series)
    Translocations = find_rearrangement_operations.TranslocationIdentification(edge_series, sequence_blocks)
    Inverted_translocations = find_rearrangement_operations.InvertedTranslocationIdentification(edge_series,sequence_blocks)


    print('Inversions: ', Inversions)
    print()
    print("Translocations: ", Translocations)
    print()
    print('Inverted translocations: ', Inverted_translocations)
    print()
    print(sequence_blocks)
    x = -10.0
    print(str(int(x)) in sequence_blocks)
    print(int(x))

    find_affected_sequence_blocks = IdentifyIncompatibleOperations()
    translocation_affected_sequence_blocks = find_affected_sequence_blocks.TranslocationAffectedSequenceBlocks(Translocations)
    inverted_translocation_affected_sequence_blocks = find_affected_sequence_blocks.InvertedTranslocationAffectedSequenceBlocks(Inverted_translocations, sequence_blocks)
    inversion_affected_sequence_blocks = find_affected_sequence_blocks.InversionAffectedSequenceBlocks(Inversions, sequence_blocks)

    print('inversion_affected_sequence_blocks: ', inversion_affected_sequence_blocks)
    print()
    print('translocation_affected_sequence_blocks: ', translocation_affected_sequence_blocks)
    print()
    print('inverted_translocation_affected_sequence_blocks: ', inverted_translocation_affected_sequence_blocks)

    find_compatible_operations = IdentifyIncompatibleOperations()
    generate_list_of_compatible_operations = find_compatible_operations.FindCompatibleOperations(Inversions, Translocations, Inverted_translocations, inversion_affected_sequence_blocks, translocation_affected_sequence_blocks, inverted_translocation_affected_sequence_blocks)

    print('inversion_affected_sequence_blocks: ', inversion_affected_sequence_blocks)
    print()
    print('translocation_affected_sequence_blocks: ', translocation_affected_sequence_blocks)
    print()
    print('inverted_translocation_affected_sequence_blocks: ', inverted_translocation_affected_sequence_blocks)

    print()
    print(generate_list_of_compatible_operations)