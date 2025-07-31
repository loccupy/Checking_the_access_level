from libs.check_attr_and_meth import *
from libs.utils import *


def check_data(data_objects, arr_obj):
    arr_obis = []

    for i in data_objects:
        arr_obis.append(i.logicalName)

    for key in arr_obj.keys():
        try:
            if key in arr_obis:
                print(f"\nПроверяется объект '{key}'...")
                check_data_atr_and_meth(data_objects, key)
            else:
                print(f'{key} "{arr_obj.get(key)}" ОТСУТСТВУЕТ В КОЛЛЕКЦИИ СЧЕТЧИКА!!!')
        except Exception as e:
            print(e)


def check_registers(register_objects, arr_obj):
    arr_obis = []

    for i in register_objects:
        arr_obis.append(i.logicalName)

    for key in arr_obj.keys():
        try:
            if key in arr_obis:
                print(f"\nПроверяется объект '{key}'...")
                check_registers_atr_and_meth(register_objects, key)
            else:
                print(f'{key} "{arr_obj.get(key)}" ОТСУТСТВУЕТ В КОЛЛЕКЦИИ СЧЕТЧИКА!!!')
        except Exception as e:
            print(e)


def check_clock(clock_objects):
    arr_obis = []

    for i in clock_objects:
        arr_obis.append(i.logicalName)

    for key in arr_obj_clock.keys():
        try:
            if key in arr_obis:
                print(f"\nПроверяется объект '{key}'...")
                check_clock_atr_and_meth(clock_objects, key)
            else:
                print(f'{key} "{arr_obj_clock.get(key)}" ОТСУТСТВУЕТ В КОЛЛЕКЦИИ СЧЕТЧИКА!!!')
        except Exception as e:
            print(e)


def check_demand_register(demand_register_objects):
    arr_obis = []

    for i in demand_register_objects:
        arr_obis.append(i.logicalName)

    for key in arr_obj_demand_register.keys():
        try:
            if key in arr_obis:
                print(f"\nПроверяется объект '{key}'...")
                check_demand_register_atr_and_meth(demand_register_objects, key)
            else:
                print(f'{key} "{arr_obj_demand_register.get(key)}" ОТСУТСТВУЕТ В КОЛЛЕКЦИИ СЧЕТЧИКА!!!')
        except Exception as e:
            print(e)


def check_profile_generic(profile_generic_objects):
    arr_obis = []

    for i in profile_generic_objects:
        arr_obis.append(i.logicalName)

    for key in arr_obj_profile_generic.keys():
        try:
            if key in arr_obis:
                print(f"\nПроверяется объект '{key}'...")
                check_profile_generic_atr_and_meth(profile_generic_objects, key)
            else:
                print(f'{key} "{arr_obj_profile_generic.get(key)}" ОТСУТСТВУЕТ В КОЛЛЕКЦИИ СЧЕТЧИКА!!!')
        except Exception as e:
            print(e)


def check_script_table(script_table_objects):
    arr_obis = []

    for i in script_table_objects:
        arr_obis.append(i.logicalName)

    for key in arr_obj_script_table.keys():
        try:
            if key in arr_obis:
                print(f"\nПроверяется объект '{key}'...")
                check_script_table_atr_and_meth(script_table_objects, key)
            else:
                print(f'{key} "{arr_obj_script_table.get(key)}" ОТСУТСТВУЕТ В КОЛЛЕКЦИИ СЧЕТЧИКА!!!')
        except Exception as e:
            print(e)


def check_special_days_table(special_days_table_objects):
    arr_obis = []

    for i in special_days_table_objects:
        arr_obis.append(i.logicalName)

    for key in arr_obj_special_days_table_objects.keys():
        try:
            if key in arr_obis:
                print(f"\nПроверяется объект '{key}'...")
                check_special_days_table_atr_and_meth(special_days_table_objects, key)
            else:
                print(f'{key} "{arr_obj_special_days_table_objects.get(key)}" ОТСУТСТВУЕТ В КОЛЛЕКЦИИ СЧЕТЧИКА!!!')
        except Exception as e:
            print(e)


def check_association_logical_name(association_logical_name_objects):
    arr_obis = []

    for i in association_logical_name_objects:
        arr_obis.append(i.logicalName)

    for key in arr_obj_association_logical_name_1ph.keys():
        try:
            if key in arr_obis:
                print(f"\nПроверяется объект '{key}'...")
                check_association_logical_name_atr_and_meth(association_logical_name_objects, key)
            else:
                print(f'{key} "{arr_obj_association_logical_name_1ph.get(key)}" ОТСУТСТВУЕТ В КОЛЛЕКЦИИ СЧЕТЧИКА!!!')
        except Exception as e:
            print(e)


def check_sap_assignment(sap_assignment_objects):
    arr_obis = []

    for i in sap_assignment_objects:
        arr_obis.append(i.logicalName)

    for key in arr_obj_sap_assignment.keys():
        try:
            if key in arr_obis:
                print(f"\nПроверяется объект '{key}'...")
                check_sap_assignment_name_atr_and_meth(sap_assignment_objects, key)
            else:
                print(f'{key} "{arr_obj_sap_assignment.get(key)}" ОТСУТСТВУЕТ В КОЛЛЕКЦИИ СЧЕТЧИКА!!!')
        except Exception as e:
            print(e)


def check_iec_local_port_setup(iec_local_port_setup_objects):
    arr_obis = []

    for i in iec_local_port_setup_objects:
        arr_obis.append(i.logicalName)

    for key in arr_obj_iec_local_port_setup_objects.keys():
        try:
            if key in arr_obis:
                print(f"\nПроверяется объект '{key}'...")
                check_iec_local_port_setup_name_atr_and_meth(iec_local_port_setup_objects, key)
            else:
                print(f'{key} "{arr_obj_iec_local_port_setup_objects.get(key)}" ОТСУТСТВУЕТ В КОЛЛЕКЦИИ СЧЕТЧИКА!!!')
        except Exception as e:
            print(e)


def check_activity_calendar(activity_calendar_objects):
    arr_obis = []

    for i in activity_calendar_objects:
        arr_obis.append(i.logicalName)

    for key in arr_obj_activity_calendar.keys():
        try:
            if key in arr_obis:
                print(f"\nПроверяется объект '{key}'...")
                check_activity_calendar_atr_and_meth(activity_calendar_objects, key)
            else:
                print(f'{key} "{arr_obj_activity_calendar.get(key)}" ОТСУТСТВУЕТ В КОЛЛЕКЦИИ СЧЕТЧИКА!!!')
        except Exception as e:
            print(e)


def check_action_schedule(action_schedule_objects):
    arr_obis = []

    for i in action_schedule_objects:
        arr_obis.append(i.logicalName)

    for key in arr_obj_action_schedule.keys():
        try:
            if key in arr_obis:
                print(f"\nПроверяется объект '{key}'...")
                check_action_schedule_atr_and_meth(action_schedule_objects, key)
            else:
                print(f'{key} "{arr_obj_action_schedule.get(key)}" ОТСУТСТВУЕТ В КОЛЛЕКЦИИ СЧЕТЧИКА!!!')
        except Exception as e:
            print(e)


def check_iec_hdlc_setup(iec_hdlc_setup_objects):
    arr_obis = []

    for i in iec_hdlc_setup_objects:
        arr_obis.append(i.logicalName)

    for key in arr_obj_iec_hdlc_setup.keys():
        try:
            if key in arr_obis:
                print(f"\nПроверяется объект '{key}'...")
                check_iec_hdlc_setup_atr_and_meth(iec_hdlc_setup_objects, key)
            else:
                print(f'{key} "{arr_obj_iec_hdlc_setup.get(key)}" ОТСУТСТВУЕТ В КОЛЛЕКЦИИ СЧЕТЧИКА!!!')
        except Exception as e:
            print(e)


def check_push_setup(push_setup_objects):
    arr_obis = []

    for i in push_setup_objects:
        arr_obis.append(i.logicalName)

    for key in arr_obj_push_setup.keys():
        try:
            if key in arr_obis:
                print(f"\nПроверяется объект '{key}'...")
                check_push_setup_atr_and_meth(push_setup_objects, key)
                # obj = push_setup_objects.findByLN(ObjectType.PUSH_SETUP, key)
                #
                # check_access_level_for_attribute(obj, 1, AccessMode.READ)
                # check_access_level_for_attribute(obj, 2, AccessMode.READ)
                # check_access_level_for_attribute(obj, 3, AccessMode.READ)
                # check_access_level_for_attribute(obj, 4, AccessMode.READ)
                # check_access_level_for_attribute(obj, 5, AccessMode.READ)
                # check_access_level_for_attribute(obj, 6, AccessMode.READ)
                # check_access_level_for_attribute(obj, 7, AccessMode.READ)
                #
                # check_access_level_for_method(obj, 1, MethodAccessMode.NO_ACCESS)
            else:
                print(f'{key} "{arr_obj_push_setup.get(key)}" ОТСУТСТВУЕТ В КОЛЛЕКЦИИ СЧЕТЧИКА!!!')
        except Exception as e:
            print(e)


def check_security_setup(security_setup_objects):
    arr_obis = []

    for i in security_setup_objects:
        arr_obis.append(i.logicalName)

    for key in arr_obj_security_setup.keys():
        try:
            if key in arr_obis:
                print(f"\nПроверяется объект '{key}'...")
                check_security_setup_atr_and_meth(security_setup_objects, key)
            else:
                print(f'{key} "{arr_obj_security_setup.get(key)}" ОТСУТСТВУЕТ В КОЛЛЕКЦИИ СЧЕТЧИКА!!!')
        except Exception as e:
            print(e)


def check_disconnect_control(disconnect_control_objects):
    arr_obis = []

    for i in disconnect_control_objects:
        arr_obis.append(i.logicalName)

    for key in arr_obj_disconnect_control.keys():
        try:
            if key in arr_obis:
                print(f"\nПроверяется объект '{key}'...")
                check_disconnect_control_atr_and_meth(disconnect_control_objects, key)
            else:
                print(f'{key} "{arr_obj_disconnect_control.get(key)}" ОТСУТСТВУЕТ В КОЛЛЕКЦИИ СЧЕТЧИКА!!!')
        except Exception as e:
            print(e)


def check_limiter(limiter_objects):
    arr_obis = []

    for i in limiter_objects:
        arr_obis.append(i.logicalName)

    for key in arr_obj_limiter.keys():
        try:
            if key in arr_obis:
                print(f"\nПроверяется объект '{key}'...")
                check_limiter_atr_and_meth(limiter_objects, key)
            else:
                print(f'{key} "{arr_obj_limiter.get(key)}" ОТСУТСТВУЕТ В КОЛЛЕКЦИИ СЧЕТЧИКА!!!')
        except Exception as e:
            print(e)
