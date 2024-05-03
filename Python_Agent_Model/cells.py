class Cell:
    
    # Id = a random ID for the cell
    # sister_chromatids = a list of the chromosomes it has!
    # parent = Id of the parent of this cell
    def __init__(self, id, sister_chromatids, parent_ID, generation = 0):
        if id == parent_ID:
            raise("Parent and Child cannot have the same ID")
        else:
            self.id = id
            self.sister_chromatids = sister_chromatids
            self.number_chromatids = len(sister_chromatids)
            self.parent = parent_ID
            self.generation = generation
    
    #Returns the sequence of all the chromosomes and sister chromatids
    def sequence(self):
        sequences = []
        for sis_chromo in self.sister_chromatids:
            sequences.append(sis_chromo.sequence())
        return(sequences)

    # Returns the sequence strings of all the chromosomes and sister chromatids
    # [sisterchromatid[chromosome[string_sequence]], ]
    def sequence_str(self):
        sequences = []
        for sis_chromo in self.sister_chromatids:
            sequences.append(sis_chromo.sequence_str())
        return(sequences)


