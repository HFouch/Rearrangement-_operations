class RearrangementOperationIdentification():

    def __init__(self):
        pass

    def __del__(self):
        pass

    def InversionIdentification(self, edge_series):
        Inversion_operations = []
        for edge_pair in range(len(edge_series)):

            current_edge_pair = edge_series[edge_pair]
            edge1 = current_edge_pair[0]
            edge2 = current_edge_pair[1]
            orientation_edge1 = edge1/abs(edge1)
            orientation_edge2 = edge2/abs(edge2)

            if abs(edge1) < abs(edge2):
                inversion_partner = ((abs(edge1)+1)*orientation_edge1*(-1), (abs(edge2)+1)*orientation_edge2*(-1))

            else:
                inversion_partner = ((abs(edge1) + -1) * orientation_edge1 * (-1), (abs(edge2) - 1) * orientation_edge2 * (-1))

            if inversion_partner in edge_series:
                x = int(inversion_partner[0])
                y = int(inversion_partner[1])
                inversion_partner = (x,y)

                Inversion_operations.append((current_edge_pair, inversion_partner))

            else:
                pass

        return Inversion_operations

    def TranslocationIdentification(self, edge_series, sequence_blocks):
        Translocation_operations = []

        for edge_pair in range(len(edge_series)):

            current_edge_pair = edge_series[edge_pair]
            print(current_edge_pair)
            edge1 = current_edge_pair[0]
            edge2 = current_edge_pair[1]
            orientation_edge1 = edge1 / abs(edge1)
            orientation_edge2 = edge2 / abs(edge2)

            if abs(edge1) < abs(edge2):
                compatible_sequence_block = (int((abs(edge1)+1)*orientation_edge1), int((abs(edge2)-1)*orientation_edge2))


            else:
                compatible_sequence_block = (int((abs(edge1) - 1) * orientation_edge1), int((abs(edge2) + 1) * orientation_edge2))

            print('cSB: ', compatible_sequence_block)
            if compatible_sequence_block[0] in sequence_blocks and compatible_sequence_block[1] in sequence_blocks:
                position_block1 = sequence_blocks.index(compatible_sequence_block[0])
                position_block2 = sequence_blocks.index(compatible_sequence_block[1])
                position_edge1 = sequence_blocks.index(edge1)

                if position_block1 < position_block2 and position_edge1 not in range(position_block1, position_block2):
                    Translocation_operations.append((current_edge_pair, compatible_sequence_block))
                else:
                    pass
            else:
                pass

        return Translocation_operations

    def InvertedTranslocationIdentification(self, edge_series, sequence_blocks):
        Inverted_Translocation_operations =[]

        for edge_pair in range(len(edge_series)):
            current_edge_pair = edge_series[edge_pair]
            edge1 = current_edge_pair[0]
            edge2 = current_edge_pair[1]
            orientation_edge1 = edge1 / abs(edge1)
            orientation_edge2 = edge2 / abs(edge2)
            print(current_edge_pair)

            if abs(edge1) < abs(edge2):
                compatible_sequence_block = int((abs(edge2)-1)*orientation_edge2*(-1)), int((abs(edge1)+1)*orientation_edge1*(-1))

            else:
                compatible_sequence_block = (int((abs(edge2) + 1) * orientation_edge2 * (-1)), int((abs(edge1) - 1) * orientation_edge1 * (-1)))

            print('IcSB: ', compatible_sequence_block)
            print(compatible_sequence_block[0])
            print(compatible_sequence_block[1])
            print()
            if compatible_sequence_block[0] in sequence_blocks and compatible_sequence_block[1] in sequence_blocks:
                position_block1 = sequence_blocks.index(compatible_sequence_block[0])
                print('pos1: ', position_block1)
                position_block2 = sequence_blocks.index(compatible_sequence_block[1])
                position_edge1 = sequence_blocks.index(edge1)

                if position_block1 < position_block2 and position_edge1 not in range(position_block1, position_block2):
                    Inverted_Translocation_operations.append((current_edge_pair, compatible_sequence_block))
                else:
                    pass
            else:
                pass


        return Inverted_Translocation_operations