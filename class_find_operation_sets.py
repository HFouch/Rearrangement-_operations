from class_defining_rearrangment_operations import RearrangementOperationIdentification
from class_defining_edge_series import EdgeSeriesAndSequenceBlocks
from class_execute_rearrangement_operations import RearrangementOperationExcecution
class IdentificationOfOperationSets():

    def __init__(self):
        pass

    def __del__(self):
        pass

    def find_operation_sets(self, sequence_blocks):

        generate_the_series_of_edges = EdgeSeriesAndSequenceBlocks()
        edge_series = generate_the_series_of_edges.GenerateEdgesSeries(sequence_blocks)
        print('Edge series:  ', edge_series)
        List_of_operation_sets = []
        operation_set_counter = 0


        if len(edge_series) != 0:


            find_rearrangement_operations = RearrangementOperationIdentification()
            Inversions = find_rearrangement_operations.InversionIdentification(edge_series)
            Translocations = find_rearrangement_operations.TranslocationIdentification(edge_series, sequence_blocks)
            Inverted_translocations = find_rearrangement_operations.InvertedTranslocationIdentification(edge_series,
                                                                                                        sequence_blocks)
            Operations = []
            Operations.extend(Inversions)
            Operations.extend(Translocations)
            Operations.extend(Inverted_translocations)

            find_operation_set = IdentificationOfOperationSets()
            excecute_operation = find_operation_set.find_current_operation_set(sequence_blocks, Operations, Inversions, Translocations, Inverted_translocations)
            operation = excecute_operation[1]
            List_of_operation_sets.append(operation)

            new_sequence_blocks = excecute_operation[0]

            find_operations = IdentificationOfOperationSets()
            find_operations.find_operation_sets(new_sequence_blocks)

        else:
            operation_set_counter += 1
            # current_operation_set.clear()
            print('List_of_operation_sets:   ', List_of_operation_sets)



    def find_current_operation_set(self, sequence_blocks, Operations, Inversions, Translocations, Inverted_translocations):

        for i in range(len(Operations)):
            current_operation = Operations[i]
            excecute_operation = RearrangementOperationExcecution()

            if current_operation in Inversions:
                classification = 'Inv'
                excecute_inversion = excecute_operation.excecute_inversion(current_operation, sequence_blocks)
                new_sequence_blocks = excecute_inversion[0]
                inversion_position = excecute_inversion[1]
                operation = (classification, current_operation, inversion_position)

                return new_sequence_blocks, operation

            if current_operation in Translocations:
                classification = 'Trn'
                excecute_translocation = excecute_operation.excecute_translocation(current_operation, sequence_blocks)
                new_sequence_blocks = excecute_translocation[0]
                translocation_position = excecute_translocation[1]
                operation = (classification, current_operation, translocation_position)

                return new_sequence_blocks, operation

            if current_operation in Inverted_translocations:
                classification = 'Inv_trn'
                excecute_inverted_translocation = excecute_operation.excecute_inverted_translocation(current_operation, sequence_blocks)
                new_sequence_blocks = excecute_inverted_translocation[0]
                inverted_translocation_position = excecute_inverted_translocation[1]
                operation = (classification, current_operation, inverted_translocation_position)

                return new_sequence_blocks, operation


