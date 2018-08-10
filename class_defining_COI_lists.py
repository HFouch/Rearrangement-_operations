class IdentifyIncompatibleOperations():

    def __init__(self):
        pass

    def __del__(self):
        pass

    def TranslocationAffectedSequenceBlocks(self, Translocations):
        Translocation_affected_sequence_blocks  = []
        for i in range (len(Translocations)):
            affected_sequence_blocks = []
            for j in range (len(Translocations[0])):
                for k in range (len(Translocations[0][0])):
                    sequence_block = Translocations[i][j][k]
                    affected_sequence_blocks.append(sequence_block)
            Translocation_affected_sequence_blocks.append(affected_sequence_blocks)


        return Translocation_affected_sequence_blocks


    def InvertedTranslocationAffectedSequenceBlocks(self, Inverted_Translocations, sequence_blocks):
        Inverted_translocation_affected_sequence_blocks = []
        for i in range (len(Inverted_Translocations)):
            affected_sequence_blocks = []
            for k in range(len(Inverted_Translocations[0][0])):
                sequence_block = Inverted_Translocations[i][0][k]
                affected_sequence_blocks.append(sequence_block)

            position_sequence_block1 = sequence_blocks.index(Inverted_Translocations[i][1][0])
            position_sequence_block2 = sequence_blocks.index(Inverted_Translocations[i][1][1])
            sequence_blocks_to_be_moved = sequence_blocks[position_sequence_block1:(position_sequence_block2+1)]

            for i in range(len(sequence_blocks_to_be_moved)):
                sequence_block = sequence_blocks_to_be_moved[i]
                affected_sequence_blocks.append(sequence_block)

            Inverted_translocation_affected_sequence_blocks.append(affected_sequence_blocks)

        return Inverted_translocation_affected_sequence_blocks


    def InversionAffectedSequenceBlocks(self, Inversions, sequence_blocks):
        Inversion_affected_sequence_blocks = []
        for i in range (len(Inversions)):

            position_sequence_block1 = sequence_blocks.index(Inversions[i][0][0])
            position_sequence_block2 = sequence_blocks.index(Inversions[i][1][1])
            affected_sequence_blocks = sequence_blocks[position_sequence_block1:(position_sequence_block2 + 1)]

            Inversion_affected_sequence_blocks.append(affected_sequence_blocks)

        return Inversion_affected_sequence_blocks


    def FindCompatibleOperations(self, Inversions, Translocations, Inverted_Translocations, Inversion_affected_sequence_blocks, Translocations_affected_sequence_blocks, Inverted_translocation_affected_sequence_blocks):
        Compatible_operations = []
        test_compatibility = IdentifyIncompatibleOperations()
        print('!!!!!: ', Inversion_affected_sequence_blocks)
        #Starting with inversions

        for i in range(len(Inversions)):
            List_of_operations = []

            List_of_operations.append(Inversions[i])
            temp = Inversion_affected_sequence_blocks
            compatibility_list = temp[i]
            print('!!!!!: ', i, Inversion_affected_sequence_blocks)


            #Scan inversions


            for j in range(len(Inversions)):

                operation = Inversions[j]
                print('COMPATIBILITY LIST: ', compatibility_list)
                print('OPERATION: ', operation)
                print('!!!!!: ', j, Inversion_affected_sequence_blocks)

                affected_sequence_blocks = Inversion_affected_sequence_blocks[j]
                print('AFFECTED BLOCK: ', affected_sequence_blocks)

                find_compatible_inversions = test_compatibility.TestOperationCompatibility(affected_sequence_blocks, compatibility_list)
                if find_compatible_inversions == 0:
                    List_of_operations.append(operation)
                    for k in range(len(affected_sequence_blocks)):
                        compatibility_list.append(affected_sequence_blocks[k])
                else:
                    pass



            #Scan translocations
            for l in range(len(Translocations_affected_sequence_blocks)):
                operation = Translocations[l]
                affected_sequence_blocks = Translocations_affected_sequence_blocks[l]

                find_compatible_translocations = test_compatibility.TestOperationCompatibility(affected_sequence_blocks, compatibility_list)
                if find_compatible_translocations == 0:
                    List_of_operations.append(operation)
                    for k in range(len(affected_sequence_blocks)):
                        compatibility_list.append(affected_sequence_blocks[k])
                else:
                    pass

            #Scan inverted translocations
            for m in range(len(Inverted_translocation_affected_sequence_blocks)):
                operation = Inverted_Translocations[m]
                affected_sequence_blocks = Inverted_translocation_affected_sequence_blocks[m]

               # test_compatibility = IdentifyIncompatibleOperations()
                find_compatible_inverted_translocations = test_compatibility.TestOperationCompatibility(affected_sequence_blocks, compatibility_list)

                if find_compatible_inverted_translocations == 0:
                    List_of_operations.append(operation)
                    for n in range(len(affected_sequence_blocks)):
                        compatibility_list.append(affected_sequence_blocks[n])
                else:
                    pass


            Compatible_operations.append(List_of_operations)

            print('list of operations: ', List_of_operations)
            print()
            print('compatibility list: ', compatibility_list)
        return Compatible_operations




    def TestOperationCompatibility(self, affected_sequence_blocks, compatibility_list):
        x = 0
        for i in range(len(affected_sequence_blocks)):
            if affected_sequence_blocks[i] not in compatibility_list:
                x = x + 0
                pass
            else:
                x = x + 1
                break
        if x == 0:
            return 0
        else:
            return 1
