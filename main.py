import machine_class as mc

machine_list = {}

def generate_machine(name):
    machine_list[name] = mc.Machine(name)
    print(machine_list)
    return machine_list[name]

def chech_input(plaintext,ciphertext, machine_1, machine_2):
    return 0
