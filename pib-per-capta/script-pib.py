from singleton.calculate_pib_per_capta_singleton import CalculatePibPerCaptaSingleton

def main():
    
    calculate = CalculatePibFactory.create_instance()

    print(calculate)

    calculate.load_file()

    calculate.load_uf_by_region()

    calculate.print_all_content()

    calculate.get_state_by_region('CO')

    calculate.get_region_by_state('Sao Paulo')

main()