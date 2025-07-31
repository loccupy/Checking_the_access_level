from gurux_dlms.enums import ObjectType
from gurux_dlms.objects import GXDLMSAssociationLogicalName, GXDLMSObjectCollection, GXDLMSData

from libs.checking import *
from libs.conftest import connect_with_access_reader
from libs.utils import merge_all_dicts, arr_obg_register_1ph, arr_obj_data_for_1ph, arr_obg_register_3ph, \
    arr_obg_register_TT, arr_obj_data_for_3ph, arr_obj_data_for_TT


def test_debug():
    reader, settings = connect_with_access_reader()
    settings.media.open()
    reader.initializeConnection()

    reader.setDeviceType()
    device_type = reader.deviceType
    serial_number = reader.read(GXDLMSData('0.0.96.1.0.255'), 2).decode('utf-8')
    proshivka = reader.read(GXDLMSData('0.0.96.1.8.255'), 2).decode('utf-8')
    reader.close()

    print('_____________________________________________________________________________')
    print(f'Проверяется счетчик типа {device_type} №{serial_number} на прошивке {proshivka}...')

    reader, settings = connect_with_access_reader()
    settings.media.open()
    reader.initializeConnection()

    object_list = reader.read(GXDLMSAssociationLogicalName('0.0.40.0.0.255'), 2)

    reader.close()

    arr_obis = []

    for i in object_list:
        arr_obis.append(i.logicalName)

    all_objects = merge_all_dicts(device_type)

    res_arr = GXDLMSObjectCollection()

    for key in arr_obis:
        if key not in all_objects.keys():
            for i in object_list:
                if key == i.logicalName:
                    res_arr.append(object_list.findByLN(i.getObjectType(), key))
                    break

    object_list = res_arr

    print("\nПроверка Clock...")
    clock_objects = object_list.getObjects(ObjectType.CLOCK)
    for i in clock_objects:
        print(f"Проверяется объект '{i.logicalName}'...")
        check_clock_atr_and_meth(clock_objects, i.logicalName)

    print("\nПроверка Registers...")
    register_objects = object_list.getObjects(ObjectType.REGISTER)
    for i in register_objects:
        print(f"Проверяется объект '{i.logicalName}'...")
        check_registers_atr_and_meth(register_objects, i.logicalName)

    print("\nПроверка Data...")
    data_objects = object_list.getObjects(ObjectType.DATA)
    for i in data_objects:
        print(f"Проверяется объект '{i.logicalName}'...")
        check_data_atr_and_meth(data_objects, i.logicalName)

    print("\nПроверка Demand Register...")
    demand_register_objects = object_list.getObjects(ObjectType.DEMAND_REGISTER)
    for i in demand_register_objects:
        print(f"Проверяется объект '{i.logicalName}'...")
        check_demand_register_atr_and_meth(demand_register_objects, i.logicalName)

    print("\nПроверка Profile Generic...")
    profile_generic_objects = object_list.getObjects(ObjectType.PROFILE_GENERIC)
    for i in profile_generic_objects:
        print(f"Проверяется объект '{i.logicalName}'...")
        check_profile_generic_atr_and_meth(profile_generic_objects, i.logicalName)

    print("\nПроверка SCRIPT_TABLE...")
    script_table_objects = object_list.getObjects(ObjectType.SCRIPT_TABLE)
    for i in script_table_objects:
        print(f"Проверяется объект '{i.logicalName}'...")
        check_script_table_atr_and_meth(script_table_objects, i.logicalName)

    print("\nПроверка SPECIAL_DAYS_TABLE...")
    special_days_table_objects = object_list.getObjects(ObjectType.SPECIAL_DAYS_TABLE)
    for i in special_days_table_objects:
        print(f"Проверяется объект '{i.logicalName}'...")
        check_special_days_table_atr_and_meth(special_days_table_objects, i.logicalName)

    print("\nПроверка ASSOCIATION_LOGICAL_NAME...")
    association_logical_name_objects = object_list.getObjects(ObjectType.ASSOCIATION_LOGICAL_NAME)
    for i in association_logical_name_objects:
        print(f"Проверяется объект '{i.logicalName}'...")
        check_association_logical_name_atr_and_meth(association_logical_name_objects, i.logicalName)

    print("\nПроверка ACTIVITY_CALENDAR...")
    activity_calendar_objects = object_list.getObjects(ObjectType.ACTIVITY_CALENDAR)
    for i in activity_calendar_objects:
        print(f"Проверяется объект '{i.logicalName}'...")
        check_activity_calendar_atr_and_meth(activity_calendar_objects, i.logicalName)

    print("\nПроверка ACTION_SCHEDULE...")
    action_schedule_objects = object_list.getObjects(ObjectType.ACTION_SCHEDULE)
    for i in action_schedule_objects:
        print(f"Проверяется объект '{i.logicalName}'...")
        check_action_schedule_atr_and_meth(action_schedule_objects, i.logicalName)

    # iec_hdlc_setup
    print("\nПроверка IEC_HDLC_SETUP...")
    iec_hdlc_setup_objects = object_list.getObjects(ObjectType.IEC_HDLC_SETUP)
    for i in iec_hdlc_setup_objects:
        print(f"Проверяется объект '{i.logicalName}'...")
        check_iec_hdlc_setup_atr_and_meth(iec_hdlc_setup_objects, i.logicalName)

    # push_setup
    print("\nПроверка PUSH_SETUP...")
    push_setup_objects = object_list.getObjects(ObjectType.PUSH_SETUP)
    for i in push_setup_objects:
        print(f"Проверяется объект '{i.logicalName}'...")
        check_push_setup_atr_and_meth(push_setup_objects, i.logicalName)

    if device_type != 'TT':
        # disconnect_control
        print("\nПроверка DISCONNECT_CONTROL...")
        disconnect_control_objects = object_list.getObjects(ObjectType.DISCONNECT_CONTROL)
        for i in disconnect_control_objects:
            print(f"Проверяется объект '{i.logicalName}'...")
            check_disconnect_control_atr_and_meth(disconnect_control_objects, i.logicalName)

        # limiter
        print("\nПроверка LIMITER...")
        limiter_objects = object_list.getObjects(ObjectType.LIMITER)
        for i in limiter_objects:
            print(f"Проверяется объект '{i.logicalName}'...")
            check_limiter_atr_and_meth(limiter_objects, i.logicalName)

    print(f'ПРОВЕРКА счетчика №{serial_number} ЗАКОНЧЕНА')
    print('_____________________________________________________________________________')


def test_spodes():
    reader, settings = connect_with_access_reader()
    settings.media.open()
    reader.initializeConnection()

    reader.setDeviceType()
    device_type = reader.deviceType
    serial_number = reader.read(GXDLMSData('0.0.96.1.0.255'), 2).decode('utf-8')
    proshivka = reader.read(GXDLMSData('0.0.96.1.8.255'), 2).decode('utf-8')
    reader.close()

    print('_____________________________________________________________________________')
    print(f'Проверяется счетчик типа {device_type} №{serial_number} на прошивке {proshivka}...')

    reader, settings = connect_with_access_reader()
    settings.media.open()
    reader.initializeConnection()

    object_list = reader.read(GXDLMSAssociationLogicalName('0.0.40.0.0.255'), 2)

    reader.close()

    if device_type == '1PH':
        arr_obg_register = arr_obg_register_1ph
        arr_obj_data = arr_obj_data_for_1ph
    elif device_type == '3PH':
        arr_obg_register = arr_obg_register_3ph
        arr_obj_data = arr_obj_data_for_3ph
    else:
        arr_obg_register = arr_obg_register_TT
        arr_obj_data = arr_obj_data_for_TT

    print("\nПроверка Clock...")
    clock_objects = object_list.getObjects(ObjectType.CLOCK)
    check_clock(clock_objects)

    print("\nПроверка Registers...")
    register_objects = object_list.getObjects(ObjectType.REGISTER)
    check_registers(register_objects, arr_obg_register)

    print("\nПроверка Data...")
    data_objects = object_list.getObjects(ObjectType.DATA)
    check_data(data_objects, arr_obj_data)

    print("\nПроверка Demand Register...")
    demand_register_objects = object_list.getObjects(ObjectType.DEMAND_REGISTER)
    check_demand_register(demand_register_objects)

    print("\nПроверка Profile Generic...")
    profile_generic_objects = object_list.getObjects(ObjectType.PROFILE_GENERIC)
    check_profile_generic(profile_generic_objects)

    print("\nПроверка SCRIPT_TABLE...")
    script_table_objects = object_list.getObjects(ObjectType.SCRIPT_TABLE)
    check_script_table(script_table_objects)

    print("\nПроверка SPECIAL_DAYS_TABLE...")
    special_days_table_objects = object_list.getObjects(ObjectType.SPECIAL_DAYS_TABLE)
    check_special_days_table(special_days_table_objects)

    print("\nПроверка ASSOCIATION_LOGICAL_NAME...")
    association_logical_name_objects = object_list.getObjects(ObjectType.ASSOCIATION_LOGICAL_NAME)
    check_association_logical_name(association_logical_name_objects)

    # Не обязательный (его и нет у нас)
    # print("\nПроверка SAP_ASSIGNMENT...")
    # sap_assignment_objects = object_list.getObjects(ObjectType.SAP_ASSIGNMENT)
    # check_sap_assignment(sap_assignment_objects)

    # 'Не обязателен при использовании прямого IEC HDLC' (его и нет у нас)
    # print("\nПроверка IEC_LOCAL_PORT_SETUP...")
    # iec_local_port_setup_objects = object_list.getObjects(ObjectType.IEC_LOCAL_PORT_SETUP)
    # check_iec_local_port_setup(iec_local_port_setup_objects)

    print("\nПроверка ACTIVITY_CALENDAR...")
    activity_calendar_objects = object_list.getObjects(ObjectType.ACTIVITY_CALENDAR)
    check_activity_calendar(activity_calendar_objects)

    print("\nПроверка ACTION_SCHEDULE...")
    action_schedule_objects = object_list.getObjects(ObjectType.ACTION_SCHEDULE)
    check_action_schedule(action_schedule_objects)

    # iec_hdlc_setup
    print("\nПроверка IEC_HDLC_SETUP...")
    iec_hdlc_setup_objects = object_list.getObjects(ObjectType.IEC_HDLC_SETUP)
    check_iec_hdlc_setup(iec_hdlc_setup_objects)

    # push_setup
    print("\nПроверка PUSH_SETUP...")
    push_setup_objects = object_list.getObjects(ObjectType.PUSH_SETUP)
    check_push_setup(push_setup_objects)

    # security_setup нет в считывателе
    # print("\nПроверка SECURITY_SETUP...")
    # security_setup_objects = object_list.getObjects(ObjectType.SECURITY_SETUP)
    # check_security_setup(security_setup_objects)

    if device_type != 'TT':
        # disconnect_control
        print("\nПроверка DISCONNECT_CONTROL...")
        disconnect_control_objects = object_list.getObjects(ObjectType.DISCONNECT_CONTROL)
        check_disconnect_control(disconnect_control_objects)

        # limiter
        print("\nПроверка LIMITER...")
        limiter_objects = object_list.getObjects(ObjectType.LIMITER)
        check_limiter(limiter_objects)

    print(f'ПРОВЕРКА счетчика №{serial_number} ЗАКОНЧЕНА')
    print('_____________________________________________________________________________')


# def test_3ph():
#     reader, settings = connect_with_access_reader()
#     settings.media.open()
#     reader.initializeConnection()
#
#     object_list = reader.read(GXDLMSAssociationLogicalName('0.0.40.0.0.255'), 2)
#
#     print("\nПроверка Clock...")
#     clock_objects = object_list.getObjects(ObjectType.CLOCK)
#     check_clock(clock_objects)
#
#     print("\nПроверка Registers...")
#     register_objects = object_list.getObjects(ObjectType.REGISTER)
#     check_registers(register_objects, arr_obg_register_3ph)
#
#     print("\nПроверка Data...")
#     data_objects = object_list.getObjects(ObjectType.DATA)
#     check_data(data_objects, arr_obj_data_for_3ph)
#
#     print("\nПроверка Demand Register...")
#     demand_register_objects = object_list.getObjects(ObjectType.DEMAND_REGISTER)
#     check_demand_register(demand_register_objects)
#
#     print("\nПроверка Profile Generic...")
#     profile_generic_objects = object_list.getObjects(ObjectType.PROFILE_GENERIC)
#     check_profile_generic(profile_generic_objects)
#
#     print("\nПроверка SCRIPT_TABLE...")
#     script_table_objects = object_list.getObjects(ObjectType.SCRIPT_TABLE)
#     check_script_table(script_table_objects)
#
#     print("\nПроверка SPECIAL_DAYS_TABLE...")
#     special_days_table_objects = object_list.getObjects(ObjectType.SPECIAL_DAYS_TABLE)
#     check_special_days_table(special_days_table_objects)
#
#     print("\nПроверка ASSOCIATION_LOGICAL_NAME...")
#     association_logical_name_objects = object_list.getObjects(ObjectType.ASSOCIATION_LOGICAL_NAME)
#     check_association_logical_name(association_logical_name_objects)
#
#     # Не обязательный (его и нет у нас)
#     # print("\nПроверка SAP_ASSIGNMENT...")
#     # sap_assignment_objects = object_list.getObjects(ObjectType.SAP_ASSIGNMENT)
#     # check_sap_assignment(sap_assignment_objects)
#
#     # 'Не обязателен при использовании прямого IEC HDLC' (его и нет у нас)
#     # print("\nПроверка IEC_LOCAL_PORT_SETUP...")
#     # iec_local_port_setup_objects = object_list.getObjects(ObjectType.IEC_LOCAL_PORT_SETUP)
#     # check_iec_local_port_setup(iec_local_port_setup_objects)
#
#     print("\nПроверка ACTIVITY_CALENDAR...")
#     activity_calendar_objects = object_list.getObjects(ObjectType.ACTIVITY_CALENDAR)
#     check_activity_calendar(activity_calendar_objects)
#
#     print("\nПроверка ACTION_SCHEDULE...")
#     action_schedule_objects = object_list.getObjects(ObjectType.ACTION_SCHEDULE)
#     check_action_schedule(action_schedule_objects)
#
#     # iec_hdlc_setup
#     print("\nПроверка IEC_HDLC_SETUP...")
#     iec_hdlc_setup_objects = object_list.getObjects(ObjectType.IEC_HDLC_SETUP)
#     check_iec_hdlc_setup(iec_hdlc_setup_objects)
#
#     # push_setup
#     print("\nПроверка PUSH_SETUP...")
#     push_setup_objects = object_list.getObjects(ObjectType.PUSH_SETUP)
#     check_push_setup(push_setup_objects)
#
#     # security_setup нет в считывателе
#     # print("\nПроверка SECURITY_SETUP...")
#     # security_setup_objects = object_list.getObjects(ObjectType.SECURITY_SETUP)
#     # check_security_setup(security_setup_objects)
#
#     # disconnect_control
#     print("\nПроверка DISCONNECT_CONTROL...")
#     disconnect_control_objects = object_list.getObjects(ObjectType.DISCONNECT_CONTROL)
#     check_disconnect_control(disconnect_control_objects)
#
#     # limiter
#     print("\nПроверка LIMITER...")
#     limiter_objects = object_list.getObjects(ObjectType.LIMITER)
#     check_limiter(limiter_objects)
#
#     reader.close()
