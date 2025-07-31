from gurux_dlms.enums import ObjectType

from libs.utils import *


def check_data_atr_and_meth(data_objects, logical_name):
    try:
        obj = data_objects.findByLN(ObjectType.DATA, logical_name)
        check_access_level_for_attribute(obj, 1, AccessMode.READ)
        check_access_level_for_attribute(obj, 2, AccessMode.READ)
    except:
        raise


def check_registers_atr_and_meth(register_objects, logical_name):
    try:
        obj = register_objects.findByLN(ObjectType.REGISTER, logical_name)
        check_access_level_for_attribute(obj, 1, AccessMode.READ)
        check_access_level_for_attribute(obj, 2, AccessMode.READ)
        check_access_level_for_attribute(obj, 3, AccessMode.READ)

        check_access_level_for_method(obj, 1, MethodAccessMode.NO_ACCESS)
    except:
        raise


def check_clock_atr_and_meth(clock_objects, logical_name):
    try:
        obj = clock_objects.findByLN(ObjectType.CLOCK, logical_name)
        check_access_level_for_attribute(obj, 1, AccessMode.READ)
        check_access_level_for_attribute(obj, 2, AccessMode.READ)
        check_access_level_for_attribute(obj, 3, AccessMode.READ)
        check_access_level_for_attribute(obj, 4, AccessMode.READ)
        check_access_level_for_attribute(obj, 5, AccessMode.READ)
        check_access_level_for_attribute(obj, 6, AccessMode.READ)
        check_access_level_for_attribute(obj, 7, AccessMode.READ)
        check_access_level_for_attribute(obj, 8, AccessMode.READ)
        check_access_level_for_attribute(obj, 9, AccessMode.READ)

        check_access_level_for_method(obj, 1, MethodAccessMode.NO_ACCESS)
        check_access_level_for_method(obj, 2, MethodAccessMode.NO_ACCESS)
        check_access_level_for_method(obj, 3, MethodAccessMode.NO_ACCESS)
        check_access_level_for_method(obj, 4, MethodAccessMode.NO_ACCESS)
        check_access_level_for_method(obj, 5, MethodAccessMode.NO_ACCESS)
        check_access_level_for_method(obj, 6, MethodAccessMode.ACCESS)
    except:
        raise


def check_demand_register_atr_and_meth(demand_register_objects, logical_name):
    try:
        obj = demand_register_objects.findByLN(ObjectType.DEMAND_REGISTER, logical_name)
        check_access_level_for_attribute(obj, 1, AccessMode.READ)
        check_access_level_for_attribute(obj, 2, AccessMode.READ)
        check_access_level_for_attribute(obj, 3, AccessMode.READ)
        check_access_level_for_attribute(obj, 4, AccessMode.READ)
        check_access_level_for_attribute(obj, 5, AccessMode.READ)
        check_access_level_for_attribute(obj, 6, AccessMode.READ)
        check_access_level_for_attribute(obj, 7, AccessMode.READ)
        check_access_level_for_attribute(obj, 8, AccessMode.READ)
        check_access_level_for_attribute(obj, 9, AccessMode.READ)

        check_access_level_for_method(obj, 1, MethodAccessMode.NO_ACCESS)
        check_access_level_for_method(obj, 2, MethodAccessMode.NO_ACCESS)
    except:
        raise


def check_profile_generic_atr_and_meth(profile_generic_objects, logical_name):
    try:
        obj = profile_generic_objects.findByLN(ObjectType.PROFILE_GENERIC, logical_name)
        check_access_level_for_attribute(obj, 1, AccessMode.READ)
        check_access_level_for_attribute(obj, 2, AccessMode.READ)
        check_access_level_for_attribute(obj, 3, AccessMode.READ)
        check_access_level_for_attribute(obj, 4, AccessMode.READ)
        check_access_level_for_attribute(obj, 5, AccessMode.READ)
        check_access_level_for_attribute(obj, 6, AccessMode.READ)
        check_access_level_for_attribute(obj, 7, AccessMode.READ)
        check_access_level_for_attribute(obj, 8, AccessMode.READ)

        check_access_level_for_method(obj, 1, MethodAccessMode.NO_ACCESS)
        if logical_name == '1.0.94.7.0.255':
            check_access_level_for_method(obj, 2, MethodAccessMode.ACCESS)
        else:
            check_access_level_for_method(obj, 2, MethodAccessMode.NO_ACCESS)
    except:
        raise


def check_script_table_atr_and_meth(script_table_objects, logical_name):
    try:
        obj = script_table_objects.findByLN(ObjectType.SCRIPT_TABLE, logical_name)
        check_access_level_for_attribute(obj, 1, AccessMode.READ)
        check_access_level_for_attribute(obj, 2, AccessMode.READ)

        check_access_level_for_method(obj, 1, MethodAccessMode.NO_ACCESS)
    except:
        raise


def check_special_days_table_atr_and_meth(special_days_table_objects, logical_name):
    try:
        obj = special_days_table_objects.findByLN(ObjectType.SPECIAL_DAYS_TABLE, logical_name)
        check_access_level_for_attribute(obj, 1, AccessMode.READ)
        check_access_level_for_attribute(obj, 2, AccessMode.READ)

        check_access_level_for_method(obj, 1, MethodAccessMode.NO_ACCESS)
        check_access_level_for_method(obj, 2, MethodAccessMode.NO_ACCESS)
    except:
        raise


def check_association_logical_name_atr_and_meth(association_logical_name_objects, logical_name):
    try:
        obj = association_logical_name_objects.findByLN(ObjectType.ASSOCIATION_LOGICAL_NAME, logical_name)
        access = (AccessMode.READ_WRITE if logical_name == '0.0.40.0.0.255' else AccessMode.READ)
        check_access_level_for_attribute(obj, 1, access)
        check_access_level_for_attribute(obj, 2, access)
        check_access_level_for_attribute(obj, 3, access)
        check_access_level_for_attribute(obj, 4, access)
        check_access_level_for_attribute(obj, 5, access)
        check_access_level_for_attribute(obj, 6, access)
        check_access_level_for_attribute(obj, 7, access)
        check_access_level_for_attribute(obj, 8, access)
        check_access_level_for_attribute(obj, 9, access)

        # access_meth = (MethodAccessMode.ACCESS if key == '0.0.40.0.0.255' else MethodAccessMode.NO_ACCESS)
        check_access_level_for_method(obj, 1, MethodAccessMode.NO_ACCESS)
        check_access_level_for_method(obj, 2, MethodAccessMode.NO_ACCESS)
        check_access_level_for_method(obj, 3, MethodAccessMode.NO_ACCESS)
        check_access_level_for_method(obj, 4, MethodAccessMode.NO_ACCESS)
    except:
        raise


def check_sap_assignment_name_atr_and_meth(sap_assignment_objects, logical_name):
    try:
        obj = sap_assignment_objects.findByLN(ObjectType.SAP_ASSIGNMENT, logical_name)
        # не выяснял сколько атрибутов и методов, объект не обязательный
        check_access_level_for_attribute(obj, 1, AccessMode.READ)
        check_access_level_for_attribute(obj, 2, AccessMode.READ)

        check_access_level_for_method(obj, 1, MethodAccessMode.NO_ACCESS)
        check_access_level_for_method(obj, 2, MethodAccessMode.NO_ACCESS)
    except:
        raise


def check_iec_local_port_setup_name_atr_and_meth(iec_local_port_setup_objects, logical_name):
    try:
        obj = iec_local_port_setup_objects.findByLN(ObjectType.IEC_LOCAL_PORT_SETUP, logical_name)
        # не выяснял сколько атрибутов и методов, 'Не обязателен при использовании прямого IEC HDLC'
        check_access_level_for_attribute(obj, 1, AccessMode.READ)
        check_access_level_for_attribute(obj, 2, AccessMode.READ)

        check_access_level_for_method(obj, 1, MethodAccessMode.NO_ACCESS)
        check_access_level_for_method(obj, 2, MethodAccessMode.NO_ACCESS)
    except:
        raise


def check_activity_calendar_atr_and_meth(activity_calendar_objects, logical_name):
    try:
        obj = activity_calendar_objects.findByLN(ObjectType.ACTIVITY_CALENDAR, logical_name)

        check_access_level_for_attribute(obj, 1, AccessMode.READ)
        check_access_level_for_attribute(obj, 2, AccessMode.READ)
        check_access_level_for_attribute(obj, 3, AccessMode.READ)
        check_access_level_for_attribute(obj, 4, AccessMode.READ)
        check_access_level_for_attribute(obj, 5, AccessMode.READ)
        check_access_level_for_attribute(obj, 6, AccessMode.READ)
        check_access_level_for_attribute(obj, 7, AccessMode.READ)
        check_access_level_for_attribute(obj, 8, AccessMode.READ)
        check_access_level_for_attribute(obj, 9, AccessMode.READ)
        check_access_level_for_attribute(obj, 10, AccessMode.READ)

        check_access_level_for_method(obj, 1, MethodAccessMode.NO_ACCESS)
    except:
        raise


def check_action_schedule_atr_and_meth(action_schedule_objects, logical_name):
    try:
        obj = action_schedule_objects.findByLN(ObjectType.ACTION_SCHEDULE, logical_name)

        check_access_level_for_attribute(obj, 1, AccessMode.READ)
        check_access_level_for_attribute(obj, 2, AccessMode.READ)
        check_access_level_for_attribute(obj, 3, AccessMode.READ)
        check_access_level_for_attribute(obj, 4, AccessMode.READ)
    except:
        raise


def check_iec_hdlc_setup_atr_and_meth(iec_hdlc_setup_objects, logical_name):
    try:
        obj = iec_hdlc_setup_objects.findByLN(ObjectType.IEC_HDLC_SETUP, logical_name)

        check_access_level_for_attribute(obj, 1, AccessMode.READ)
        check_access_level_for_attribute(obj, 2, AccessMode.READ)
        check_access_level_for_attribute(obj, 3, AccessMode.READ)
        check_access_level_for_attribute(obj, 4, AccessMode.READ)
        check_access_level_for_attribute(obj, 5, AccessMode.READ)
        check_access_level_for_attribute(obj, 6, AccessMode.READ)
        check_access_level_for_attribute(obj, 7, AccessMode.READ)
        check_access_level_for_attribute(obj, 8, AccessMode.READ)
        check_access_level_for_attribute(obj, 9, AccessMode.READ)
    except:
        raise


def check_push_setup_atr_and_meth(push_setup_objects, logical_name):
    try:
        obj = push_setup_objects.findByLN(ObjectType.PUSH_SETUP, logical_name)

        check_access_level_for_attribute(obj, 1, AccessMode.READ)
        check_access_level_for_attribute(obj, 2, AccessMode.READ)
        check_access_level_for_attribute(obj, 3, AccessMode.READ)
        check_access_level_for_attribute(obj, 4, AccessMode.READ)
        check_access_level_for_attribute(obj, 5, AccessMode.READ)
        check_access_level_for_attribute(obj, 6, AccessMode.READ)
        check_access_level_for_attribute(obj, 7, AccessMode.READ)

        check_access_level_for_method(obj, 1, MethodAccessMode.NO_ACCESS)
    except:
        raise


def check_security_setup_atr_and_meth(security_setup_objects, logical_name):
    try:
        obj = security_setup_objects.findByLN(ObjectType.SECURITY_SETUP, logical_name)

        check_access_level_for_attribute(obj, 1, AccessMode.READ)

        check_access_level_for_method(obj, 1, MethodAccessMode.NO_ACCESS)
    except:
        raise


def check_disconnect_control_atr_and_meth(disconnect_control_objects, logical_name):
    try:
        obj = disconnect_control_objects.findByLN(ObjectType.DISCONNECT_CONTROL, logical_name)

        check_access_level_for_attribute(obj, 1, AccessMode.READ)
        check_access_level_for_attribute(obj, 2, AccessMode.READ)
        check_access_level_for_attribute(obj, 3, AccessMode.READ)
        check_access_level_for_attribute(obj, 4, AccessMode.READ)

        check_access_level_for_method(obj, 1, MethodAccessMode.NO_ACCESS)
        check_access_level_for_method(obj, 2, MethodAccessMode.NO_ACCESS)
    except:
        raise


def check_limiter_atr_and_meth(limiter_objects, logical_name):
    try:
        obj = limiter_objects.findByLN(ObjectType.LIMITER, logical_name)

        check_access_level_for_attribute(obj, 1, AccessMode.READ)
        check_access_level_for_attribute(obj, 2, AccessMode.READ)
        check_access_level_for_attribute(obj, 3, AccessMode.READ)
        check_access_level_for_attribute(obj, 4, AccessMode.READ)
        check_access_level_for_attribute(obj, 5, AccessMode.READ)
        check_access_level_for_attribute(obj, 6, AccessMode.READ)
        check_access_level_for_attribute(obj, 7, AccessMode.READ)
        check_access_level_for_attribute(obj, 8, AccessMode.READ)
        check_access_level_for_attribute(obj, 9, AccessMode.READ)
        check_access_level_for_attribute(obj, 10, AccessMode.READ)
        check_access_level_for_attribute(obj, 11, AccessMode.READ)
    except:
        raise
