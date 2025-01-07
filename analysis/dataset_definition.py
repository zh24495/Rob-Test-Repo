from ehrql import create_dataset, codelist_from_csv,show
from ehrql.tables.tpp import (
    addresses,
    apcs,
    apcs_cost,
    appointments,
    clinical_events,
    clinical_events_ranges,
    covid_therapeutics,
    ec,
    ec_cost,
    emergency_care_attendances,
    ethnicity_from_sus,
    household_memberships_2020,
    medications,
    occupation_on_covid_vaccine_record,
    ons_deaths,
    opa,
    opa_cost,
    opa_diag,
    opa_proc,
    open_prompt,
    parents,
    patients,
    practice_registrations,
    sgss_covid_all_tests,
    ukrr,
    vaccinations,
    wl_clockstops,
    wl_openpathways,
)
dementia_codelist = codelist_from_csv(
    "codelists/bristol-any-dementia-snomed-ct-v14.csv",column="code"
)

dataset = create_dataset()
dataset.configure_dummy_data(population_size=1000)

dataset.define_population(patients.date_of_birth.is_on_or_before("2025-01-06"))

dataset.sex = patients.sex
dataset.date_of_birth = patients.date_of_birth
dataset.number_of_medications=medications.except_where(medications.dmd_code=='39113611000001102').count_for_patient()
dataset.date_of_diagnosis = (
    clinical_events.where(clinical_events.snomedct_code.is_in(dementia_codelist))
    .sort_by(clinical_events.date)
    .first_for_patient()
    .date
)
dataset.dementiacode = (
    clinical_events.where(clinical_events.snomedct_code.is_in(dementia_codelist))
    .sort_by(clinical_events.date)
    .first_for_patient()
    .snomedct_code
)

show(medications)
#index_date = "2020-03-31"

#has_registration = practice_registrations.for_patient_on(
#    index_date
#).exists_for_patient()