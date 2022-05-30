
def atom_lister(filename):
    with open(filename,'r') as protein:
        mass_list = []
        for line in protein:
            new_mass = line.split(" ")[0]
            mass_list.append(new_mass)
    return mass_list


def xcom(filename):
    with open(filename,'r') as protein:
        mass_list = []
        for line in protein:
            new_mass = line.split(" ")[1]
            mass_list.append(new_mass)
    return mass_list


def ycom(filename):
    with open(filename,'r') as protein:
        mass_list = []
        for line in protein:
            new_mass = line.split(" ")[2]
            mass_list.append(new_mass)
    return mass_list


def zcom(filename):
    with open(filename,'r') as protein:
        mass_list = []
        for line in protein:
            new_mass = line.split(" ")[3]
            mass_list.append(new_mass)
    return mass_list


def makemassdict(atom_mass_file):
    with open(atom_mass_file,'r') as atom_mass:
        new_atom = []
        new_mass = []
        for line in atom_mass:
            new_atom.append(line.split(" ")[0])
            new_mass.append(line.split(" ")[1])
        new_dict = {new_atom[i]: new_mass[i] for i in range(len(new_mass))}
    return new_dict


def com_sum(atom_dict, atoms_list, coord_list):
    temp_coord = 0.0
    temp_mass = 0.0
    for i in range(len(coord_list)):
        temp_coord = temp_coord + (float(atom_dict.get(atoms_list[i])) * float(coord_list[i]))
        temp_mass = temp_mass + float(atom_dict.get(atoms_list[i]))
    return float(temp_coord) / float(temp_mass)


if __name__ == "__main__":
    massDict = makemassdict("atom_mass_file")
    atom_list = atom_lister('proteinCoordsMass')
    xCoords = xcom('proteinCoordsMass')
    yCoords = ycom('proteinCoordsMass')
    zCoords = zcom('proteinCoordsMass')

    xCOM = com_sum(massDict, atom_list,xCoords)
    yCOM = com_sum(massDict, atom_list,yCoords)
    zCOM = com_sum(massDict, atom_list,zCoords)
    print("xCOM, yCOM, zCOM:"+ str(xCOM) + ", " + str(yCOM) + ", " + str(zCOM))