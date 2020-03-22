class InvestmentProperty:
    REQUIRED_KW_ARGS = []
    #####################################
    # Required args for instantiation:
    #####################################
    # property (dict):
        # list_price=float
        # maintenance_costs_monthly:float
        # other_costs_monthly:float
        # property_tax_annual:float
        # rent_annual:float

    # land_transfer_tax (dict):
        # country:string
        # province:string
        # city:string

    # property_economic (dict):
        # annual_list_price_growth
        # annual_maintenance_costs_growth_rate=float
        # annual_other_costs_growth_rate=float
        # annual_property_tax_growth_rate=float
        # annual_rent_growth_rate=float

    # mortgage (dict):
        # percent_down=float
        # interest_rate_apr=float
        # term_years=int
        # months_prepayment_fee=int

    # transaction (dict):
        # holding period=int
        # legal_fees_purchase=float
        # legal_fees_sale=float
        # other_fees_purchase=float
        # other_fees_sale=float
        # agent_fees_percent_on_sale=float

    # Fees reminder: https://zinatikay.com/buying-a-house-in-ontario-prepare-for-these-fees/

    def __init__(self, **kwargs):
        pass