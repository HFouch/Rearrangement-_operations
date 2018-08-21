class RearrangementOperationExcecution():
    def __init__(self):
        pass
    def __del__(self):
        pass

    def excecute_inversion(self, inversion, sequence_blocks):

        temp = sequence_blocks[sequence_blocks.index(inversion[0][1]):sequence_blocks.index(inversion[1][0])+1]

        inverted_sequence = []
        for i in range(len(temp)):
            current_sequence_block = temp[i]*(-1)
            inverted_sequence.append(current_sequence_block)

        new_sequence_blocks = sequence_blocks[:sequence_blocks.index(inversion[0][0])+1] + inverted_sequence[::-1] + sequence_blocks[sequence_blocks.index(inversion[1][1]):]
        inversion_position = (sequence_blocks.index(inversion[0][1])+1, sequence_blocks.index(inversion[1][0])+1)

        return new_sequence_blocks, inversion_position

    def excecute_translocation(self, translocation, sequence_blocks):

        temp = sequence_blocks[sequence_blocks.index(translocation[1][0]):sequence_blocks.index(translocation[1][1])+1]

        temp_sequence_blocks = sequence_blocks[:sequence_blocks.index(translocation[1][0])] + sequence_blocks[sequence_blocks.index(translocation[1][1])+1:]

        new_sequence_blocks = temp_sequence_blocks[:temp_sequence_blocks.index(translocation[0][0])+1] + temp[::] + temp_sequence_blocks[temp_sequence_blocks.index(translocation[0][1]):]

        translocation_position = (sequence_blocks.index(translocation[0][0])+1, (sequence_blocks.index(translocation[1][0])+1, sequence_blocks.index(translocation[1][1])+1))
        return new_sequence_blocks, translocation_position

    def excecute_inverted_translocation(self, inverted_translocation, sequence_blocks):
        temp = sequence_blocks[sequence_blocks.index(inverted_translocation[1][0]):sequence_blocks.index(inverted_translocation[1][1])+1]
        inverted_sequence = []
        for i in range(len(temp)):
            current_sequence_block = temp[i]*(-1)
            inverted_sequence.append(current_sequence_block)
        temp_sequence_blocks = sequence_blocks[:sequence_blocks.index(inverted_translocation[1][0])] + sequence_blocks[sequence_blocks.index(inverted_translocation[1][1])+1:]
        new_sequence_blocks  = temp_sequence_blocks[:temp_sequence_blocks.index(inverted_translocation[0][0])+1] +inverted_sequence[::-1] + temp_sequence_blocks[temp_sequence_blocks.index(inverted_translocation[0][1]):]

        inverted_translocation_position = (sequence_blocks.index(inverted_translocation[0][0])+1, (sequence_blocks.index(inverted_translocation[1][0])+1, sequence_blocks.index(inverted_translocation[1][1])+1))

        return new_sequence_blocks, inverted_translocation_position