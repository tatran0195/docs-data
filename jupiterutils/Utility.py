from jupiterutils.PSJ_Interpreter import RUN_FILE, RUN_DEBUG, RUN_CODE
import win32gui

########################################################################
# PSJ Utilities
########################################################################

def JPT_RUN_LINE(message):
    return RUN_DEBUG(message, False)

def JPT_RUN_FILE(message):
    RUN_FILE(message, False)

def JPT_RUN_CODE(message):
    RUN_CODE(message, False)

class AssociateType:
    values = "JPT.AssociateType.values"
    AS_BARBODY = 0
    AS_BODY = 1
    AS_FACE = 2
    AS_EDGE = 3
    AS_ELEM = 4
    AS_ELEM1D = 5
    AS_SOLIDELEM = 6
    AS_NODE = 7
    AS_CONNECTION = 8
    AS_MASS = 9
    AS_CONTACT = 10
    AS_GROUP = 11
    
class BoolType:
    values = "JPT.BoolType.values"
    FALSE_VAL = 0
    TRUE_VAL = 1
    
class DItemType:
    values = "JPT.DItemType.values"
    UNKNOWN = 0
    PROJECT = 1
    INST = 2
    BODY = 3
    VERTEX = 4
    EDGE = 5
    FACE = 6
    SOLID = 7
    SHAPELINK = 8
    BODYLINK = 9
    NODE = 10
    ELEM = 11
    REF_BODY = 12
    REF_VERTEX = 13
    REF_EDGE = 14
    REF_FACE = 15
    REF_SOLID = 16
    REF_SHAPELINK = 17
    REF_BODYLINK = 18
    REF_NODE = 19
    REF_ELEM = 20
    LOCAL_SETTING = 21
    MATERIAL = 22
    ENTITY_ATTR_CAD_INFO = 23
    FEM_FIELD_SCALAR = 24
    FEM_FIELD_VECTOR = 25
    FEM_FIELD_TENSOR = 26
    COORD = 27
    LOADCASE = 28
    LBC_FORCE = 29
    LBC_FORCE_ND = 30
    LBC_FORCE_QUADRATIC = 31
    LBC_FORCE_SINE = 32
    LBC_FORCE_VECTOR = 33
    LBC_NOLIN1 = 34
    LBC_NOLIN3 = 35
    LBC_NOLIN4 = 36
    LBC_CONSTRAINT = 37
    LBC_ENFORCED_DISP = 38
    LBC_GRAVITY = 39
    LBC_G_PRESSURE = 40
    LBC_H_PRESSURE = 41
    LBC_T_PRESSURE = 42
    LBC_PRESSURE_QUADRATIC = 43
    LBC_PRESSURE_SINE = 44
    LBC_T_CENTRIFUGAL_FORCE = 45
    LBC_CS_CENTRIFUGAL_FORCE = 46
    LBC_TEMP_INI = 47
    LBC_TEMP_LOAD = 48
    LBC_TEMP_LOAD_GENERAL = 49
    LBC_TEMP_LOAD_ADVC_FILE = 50
    LBC_TEMP_LOAD_NASTRAN = 51
    LBC_TEMP_LOAD_ADVC_RESULT_REFERENCE = 52
    LBC_TEMP_BOUNDARY = 53
    LBC_CONCENTRATE_FLUX = 54
    LBC_SURFACE_FLUX = 55
    LBC_THERMAL_CONVECTION = 56
    LBC_ENFORCED_VELOCITY = 57
    LBC_ENFORCED_ACCELERATION = 58
    LBC_DYNAMIC_INITIAL_CONDITION = 59
    LBC_CONTACT_CLEARANCE = 60
    LBC_MAPPING_PRESSURE = 61
    LBC_MAPPING_FORCE = 62
    LBC_MAPPING_TEMP_LOAD = 63
    LBC_MAPPING_TEMP_BOUNDARY = 64
    LBC_MAPPING_THERMAL_CONVECTION = 65
    LBC_INITSTRESS_GENERAL = 66
    LBC_INITSTRESS_MAPPING = 67
    LBC_PRETENSION = 68
    LBC_PRETENSION_ABAQUS = 69
    LBC_SURFACE_LOADS = 70
    LBC_SUBMODEL_FORCED_DISP = 71
    LBC_SUBMODEL_FORCED_TEMP = 72
    LBC_SUBMODEL_FORCED_FLUX = 73
    LBC_INSIDE_HEAT_GENERATION = 74
    LBC_RIGIDWALL = 75
    LBC_INIT_ANGULAR_VEL_ABAQUS = 76
    LBC_WELD = 77
    SUP_GROUP = 78
    GROUP = 79
    ELEMEDGE_GROUP = 80
    FIELD_DATA = 81
    PROPERTY_0D_MASS = 82
    PROPERTY_1D_BAR = 83
    PROPERTY_1D_BEAM = 84
    PROPERTY_1D_ROD = 85
    PROPERTY_1D_PLOT = 86
    PROPERTY_2D_SHELL = 87
    PROPERTY_2D_COMPOSITE_SHELL = 88
    PROPERTY_3D_SOLID = 89
    PROPERTY_3D_GASKET = 90
    PROPERTY_3D_COHESIVE = 91
    PROPERTY_3D_WELDBEAD = 92
    SECTION_GENERAL = 93
    SECTION_LIBRARY = 94
    SECTION_SKETCHER = 95
    CONNECT_MPC = 96
    CONNECT_SPRING = 97
    CONNECT_RBE2 = 98
    CONNECT_CONM = 99
    CONNECT_PROD = 100
    CONNECT_RBAR = 101
    CONNECT_RBE3 = 102
    CONNECT_BUSH = 103
    CONNECT_MOMENT = 104
    CONNECT_WELD = 105
    CONNECT_DAMPER = 106
    CONNECT_CONNECTOR = 107
    CONTACT_ADVC = 108
    CONTACT_NXNASTRAN = 109
    CONTACT_MSCNASTRAN = 110
    CONTACT_ABAQUS = 111
    CONTACT_ANSYS = 112
    CONTACT = 113
    CUSTOM_ATTR_STRING = 114
    CUSTOM_ATTR_VECTOR = 115
    CUSTOM_ATTR_DOUBLE = 116
    DCS = 117
    ADVCPROCESS = 118
    ADVCPROCESS_STATIC = 119
    ADVCPROCESS_DYNAMIC = 120
    ADVCPROCESS_EIGEN = 121
    ADVCPROCESS_CREEP = 122
    ADVCPROCESS_DYNAMIC_EXPLICIT = 123
    ADVCPROCESS_FATIGUE = 124
    ADVCPROCESS_MODAL_FREQ_RESP = 125
    ADVCPROCESS_RESP_SPEC = 126
    ADVCPROCESS_RAND_RESP = 127
    ADVCPROCESS_SSH = 128
    ADVCPROCESS_TH = 129
    ADVCJOB = 130
    ABAQSTEPS = 131
    ABAQSTEPS_STRUCT = 132
    ABAQSTEPS_THERMAL = 133
    ABAQSTEPS_STRUCT_STATIC = 134
    ABAQSTEPS_STRUCT_FREQUENCY = 135
    ABAQSTEPS_STRUCT_COUPLEDTD = 136
    ABAQSTEPS_STRUCT_DYNAMIC = 137
    ABAQSTEPS_STRUCT_DYNAMIC_COUPLEDTD = 138
    ABAQSTEPS_STRUCT_DYNAMIC_EXPLICIT = 139
    ABAQSTEPS_STRUCT_STATICRISK = 140
    ABAQSTEPS_THERMAL_SS = 141
    ABAQSTEPS_THERMAL_TRANSIENT = 142
    ABAQUSJOB = 143
    LBC_MAPPING_HEATFLUX = 144
    CONNECT_GAP = 145
    ANSYSJOB = 146
    NASTRANJOB = 147
    DYANAMISJOB = 148
    WELDORDER = 149
    ATTRIBUTE_FXWELD = 150
    ACTRANJOB = 151
    LSDYNAJOB = 152
    NCS = 153
    ATTRIBUTE_PS_BLENDSURFACE = 154
    LBC_DOFSET = 155
    BEAM_PROP_ATTR = 156
    BEAM_PROP_ATTR2 = 157
    SHELL_PROP_ATTR = 158
    CONN_PROP_ATTR = 159
    LBC_PRETENSION_NXN = 160
    LBC_MAPPING_TEMP_MARINE_ENGINE = 161
    USER_PROP = 162
    CONNECTION_ELEMENT = 163
    CONTACT_TSSS = 164
    LBC_MAPPING_FORCEDDISPLACEMENT = 165
    LBC_MAPPING_FORCED_TEMP = 166
    NASTRAN_POSTJOB = 167
    ADVC2_POSTJOB = 168
    USER_RESULT = 169
    LBC_PRETENSION_ADVC = 170
    CONTACT_TSSOLVER = 171
    NASTRAN_HDF5_POSTJOB = 172
    PERMASJOB = 173
    LBC_MAPPING_TEMP_INIT = 174
    PROPERTY_2D_RIGID_BODY = 175
    LBC_PRETENSION_SUNSHINE = 176
    LBC_RADIATION = 177
    LBC_THERMAL_ATTRIBUTES = 178
    CONTACT_PERMAS = 179
    FRONTISTRJOB = 180
    FRONTISTRSTEP = 181
    UNV_POSTJOB = 182
    TSV_POSTJOB = 183
    MARCJOB = 184
    MARCSTEPS_STRUCT_STATIC = 185
    MARCSTEPS_STRUCT_FREQUENCY = 186
    MARCSTEPS_THERMAL_SS = 187
    MARCSTEPS_THERMAL_TRANSIENT = 188
    PERIDYNAMIC_MODEL = 189
    PD_BODY_FORCE = 190
    PERIDYNAMIC_FRACTURE_MODEL = 191
    POST_NODE = 192
    POST_ELEM = 193
    POST_RESULT_CURVE = 194
    POST_FREQ_ANALYSIS = 195
    POST_FREQ_RESULT_CURVE = 196
    POST_FREQ_LOAD = 197
    POST_FREQ_LOADCASE = 198
    POST_FREQ_RESPONSE = 199
    POST_FREQ_INTERACTIVE_LOAD_AND_RESPONSE = 200
    POST_FREQ_RESULT_MPF_CURVE = 201
    POST_TRANS_ANALYSIS = 202
    POST_TRANS_RESULT_CURVE = 203
    POST_TRANS_LOAD = 204
    POST_TRANS_LOADCASE = 205
    POST_TRANS_RESPONSE = 206
    POST_TRANS_RESULT_MPF_CURVE = 207
    POST_BTXBTA = 208
    POST_ACTRAN_ANALYSIS = 209
    POST_ACTRAN_DOMAIN_GROUP = 210
    POST_ACTRAN_DOMAIN = 211
    POST_ACTRAN_SURFACE_GROUP = 212
    POST_ACTRAN_SURFACE = 213
    POST_ACTRAN_POINT_GROUP = 214
    POST_ACTRAN_POINT = 215
    POST_ACTRAN_LOADCASE = 216
    CUSTOM_TAS_RAO = 217
    POST_GURURI_RESPONSE = 218
    POST_GURURI_SWEEP = 219
    POST_FFT_CONDITION = 220
    POST_FREQ_ANALYSIS_SOLVER = 221
    POST_FREQ_LOAD_SOLVER = 222
    POST_FREQ_RESPONSE_SOLVER = 223
    POST_FREQ_INTERACTIVE_ANALYSIS = 224
    POST_MBD_FATIGUE_ANALYSIS = 225
    POST_MBD_FATIGUE_RESULT = 226
    POST_MBD_FATIGUE_THERMAL_STRESS = 227
    POST_MBD_FATIGUE_NODAL_TEMPERATURE = 228
    POST_MBD_FATIGUE_PROPERTY = 229
    POST_MBD_FATIGUE_CONDITION = 230
    CONNECT_LINEARGAP = 231
    OPTISHAPE_TS_JOB = 232
    POST_MBD_FATIGUE_STRESS_RECOVERY = 233
    CONTACT_FRONTISTR = 234
    POST_ACTRAN_CONTRIBUTION_RESULT_CURVE = 235
    POST_MAC_SENSOR = 236
    POST_MAC_SENSOR_COLLECTION = 237
    POST_SURFACE_DISTANCE = 238
    CUSTOM_SESSION = 239
    POST_ACOUSTIC_TRANSMISSION_LOSS = 240
    POST_ACOUSTIC_TL_PCH_RESULT = 241
    POST_ACOUSTIC_TL_CONDITION = 242
    POST_ACOUSTIC_TRANSMISSION_LOSS_CONDITION_CURVE = 243
    CUSTOM_SESSION_NAGISA = 244
    PD_JOB = 245
    WAON_ANALYSIS_JOB = 246
    POST_MAC_DATA = 247
    POST_ROUGH_SURF = 248
    POST_MAC_FACTOR_CALCULATION = 249
    VIRTUAL_FLUID_MASS = 250
    PD_CURVE = 251
    PD_PERIDYNAMIC_MATERIAL = 252
    PD_FRACTURE_MODEL = 253
    PD_PART = 254
    PD_BOUNDARY_CONDITION = 255
    PD_LOAD_CONDITION = 256
    PD_SOLVER = 257
    PD_EXPORT_SETTING = 258
    CONTACT_LSDYNA = 259
    ADVCPROCESS_RDNLK = 260
    WAON_STRUCTURE_MANAGER = 261
    WAON_SOUNDSOURCE_MANAGER = 262
    WAON_ABSORPTION_MANAGER = 263
    POST_FATIGUE_MATERIAL = 264
    WAON_FIELDCAL_MANAGER = 265
    WAON_TRANSFERFUNC_MANAGER = 266
    POST_RESULT_TREE_RENAME = 267
    PD_CONTACT_MODEL = 268
    PD_CRACK_MODEL = 269
    CUSTOM_NOTE = 270
    CUSTOM_NOTE_COLLECTION = 271
    POST_TRANS_ANALYSIS_SOLVER = 272
    POST_TRANS_LOAD_SOLVER = 273
    POST_TRANS_RESPONSE_SOLVER = 274
    LBC_ACCELERATION_LOAD_ACCEL = 275
    LBC_ACCELERATION_LOAD_ACCEL1 = 276
    LBC_ENFORCED_RELATIVE_DISP = 277
    MEASURE_NOTE = 278
    MEASURE_NOTE_COLLECTION = 279
    LBC_MUFFLER_T_CONVECTION = 280
    LBC_MUFFLER_T_TEMP_LOAD = 281
    POST_RESULT_TREE_DELETED = 282
    LBC_PRETENSION_MSC_NASTRAN = 283
    LBC_PRESCRIBED_MOTION = 284
    DAMPING_PART_STIFFNESS = 285
    CONNECT_RBC = 286
    POST_ERP = 287
    POST_PLOT_ERP = 288
    LBC_COIL = 289
    LBC_THERMAL_SHELL_CONVECTION = 290
    LBC_EXTERNAL_CURRENT_DENSITY = 291
    LBC_ELECTROMAGNETIC_BC = 292
    LBC_SURFACE_CURRENT_DENSITY = 293
    LBC_ELECTRIC_POTENTIAL = 294
    END = 307
    
class DTableType:
    values = "JPT.DTableType.values"
    DTABLE_UNKNOWN = 0
    DTABLE_SHAPE = 3
    DTABLE_BODY = 5
    DTABLE_NODE = 7
    DTABLE_ELEM = 8
    DTABLE_LOCAL_SETTING = 15
    DTABLE_MATERIAL = 16
    DTABLE_COORDINATE = 18
    DTABLE_LOADCASE = 19
    DTABLE_LBC_START = 20
    DTABLE_LBC_END = 55
    DTABLE_FIELD_DATA = 56
    DTABLE_SUP_GROUP = 58
    DTABLE_GROUP = 59
    DTABLE_ELEMEDGE_GROUP = 60
    DTABLE_PROPERTY = 61
    DTABLE_SECTION = 62
    DTABLE_CONNECTION = 63
    DTABLE_CONTACT = 64
    DTABLE_CUSTOM_ATTRIBUTE = 65
    DTABLE_ADVCPROCESS = 67
    DTABLE_ADVCJOB = 68
    DTABLE_ABAQSTEPS = 69
    DTABLE_ABAQUSJOB = 70
    DTABLE_ANSYSJOB = 71
    DTABLE_NASTRANJOB = 72
    DTABLE_DYNAMISJOB = 73
    DTABLE_ACTRANJOB = 75
    DTABLE_LSDYNAJOB = 76
    DTABLE_LBC_DOFSET = 79
    DTABLE_USER_PROPERTY = 84
    DTABLE_POSTJOB = 86
    DTABLE_USER_RESULT = 87
    DTABLE_POST_NODE = 96
    DTABLE_POST_ELEM = 97
    DTABLE_POST_SURFACE_DISTANCE = 130
    DTABLE_CUSTOM_NOTE = 154
    DTABLE_CUSTOM_NOTE_COLLECTION = 155
    DTABLE_MEASURE_NOTE = 160
    DTABLE_MEASURE_NOTE_COLLECTION = 161
    
class ElemKind:
    values = "JPT.ElemKind.values"
    ELEMKIND_UNKNOWN = 0
    ELEMKIND_0D = 1
    ELEMKIND_1D = 2
    ELEMKIND_2D = 3
    ELEMKIND_3D = 4
    ELEMKIND_SP = 5
    
class ElemType:
    values = "JPT.ElemType.values"
    ELEMTYPE_UNKNOWN = 0
    ELEMTYPE_POINT = 1
    ELEMTYPE_LINE2 = 2
    ELEMTYPE_LINE3 = 3
    ELEMTYPE_TRI3 = 4
    ELEMTYPE_TRI6 = 5
    ELEMTYPE_QUAD4 = 6
    ELEMTYPE_QUAD8 = 7
    ELEMTYPE_TET4 = 8
    ELEMTYPE_TET10 = 9
    ELEMTYPE_HEX8 = 10
    ELEMTYPE_HEX20 = 11
    ELEMTYPE_PRISM6 = 12
    ELEMTYPE_PRISM15 = 13
    ELEMTYPE_PYRAMID5 = 14
    ELEMTYPE_PYRAMID13 = 15
    ELEMTYPE_PLOT = 16
    ELEMTYPE_QUAD6 = 17
    ELEMTYPE_QUAD9 = 18
    ELEMTYPE_PRISM12 = 19
    ELEMTYPE_HEX18 = 20
    ELEMTYPE_RBE = 21
    ELEMTYPE_MASS = 22
    ELEMTYPE_VIRTUAL = 23
    
class EntityType:
    values = "JPT.EntityType.values"
    UNKNOWN = 0
    PROJECT = 1
    INST = 2
    BODY = 3
    VERTEX = 4
    EDGE = 5
    FACE = 6
    SOLID = 7
    SHAPELINK = 8
    BODYLINK = 9
    NODE = 10
    ELEM = 11
    REF_BODY = 12
    REF_VERTEX = 13
    REF_EDGE = 14
    REF_FACE = 15
    REF_SOLID = 16
    REF_SHAPELINK = 17
    REF_BODYLINK = 18
    REF_NODE = 19
    REF_ELEM = 20
    LOCAL_SETTING = 21
    MATERIAL = 22
    ENTITY_ATTR_CAD_INFO = 23
    FEM_FIELD_SCALAR = 24
    FEM_FIELD_VECTOR = 25
    FEM_FIELD_TENSOR = 26
    COORD = 27
    LOADCASE = 28
    LBC_FORCE = 29
    LBC_FORCE_ND = 30
    LBC_FORCE_QUADRATIC = 31
    LBC_FORCE_SINE = 32
    LBC_FORCE_VECTOR = 33
    LBC_NOLIN1 = 34
    LBC_NOLIN3 = 35
    LBC_NOLIN4 = 36
    LBC_CONSTRAINT = 37
    LBC_ENFORCED_DISP = 38
    LBC_GRAVITY = 39
    LBC_G_PRESSURE = 40
    LBC_H_PRESSURE = 41
    LBC_T_PRESSURE = 42
    LBC_PRESSURE_QUADRATIC = 43
    LBC_PRESSURE_SINE = 44
    LBC_T_CENTRIFUGAL_FORCE = 45
    LBC_CS_CENTRIFUGAL_FORCE = 46
    LBC_TEMP_INI = 47
    LBC_TEMP_LOAD = 48
    LBC_TEMP_LOAD_GENERAL = 49
    LBC_TEMP_LOAD_ADVC_FILE = 50
    LBC_TEMP_LOAD_NASTRAN = 51
    LBC_TEMP_LOAD_ADVC_RESULT_REFERENCE = 52
    LBC_TEMP_BOUNDARY = 53
    LBC_CONCENTRATE_FLUX = 54
    LBC_SURFACE_FLUX = 55
    LBC_THERMAL_CONVECTION = 56
    LBC_ENFORCED_VELOCITY = 57
    LBC_ENFORCED_ACCELERATION = 58
    LBC_DYNAMIC_INITIAL_CONDITION = 59
    LBC_CONTACT_CLEARANCE = 60
    LBC_MAPPING_PRESSURE = 61
    LBC_MAPPING_FORCE = 62
    LBC_MAPPING_TEMP_LOAD = 63
    LBC_MAPPING_TEMP_BOUNDARY = 64
    LBC_MAPPING_THERMAL_CONVECTION = 65
    LBC_INITSTRESS_GENERAL = 66
    LBC_INITSTRESS_MAPPING = 67
    LBC_PRETENSION = 68
    LBC_PRETENSION_ABAQUS = 69
    LBC_SURFACE_LOADS = 70
    LBC_SUBMODEL_FORCED_DISP = 71
    LBC_SUBMODEL_FORCED_TEMP = 72
    LBC_SUBMODEL_FORCED_FLUX = 73
    LBC_INSIDE_HEAT_GENERATION = 74
    LBC_RIGIDWALL = 75
    LBC_INIT_ANGULAR_VEL_ABAQUS = 76
    LBC_WELD = 77
    SUP_GROUP = 78
    GROUP = 79
    ELEMEDGE_GROUP = 80
    FIELD_DATA = 81
    PROPERTY_0D_MASS = 82
    PROPERTY_1D_BAR = 83
    PROPERTY_1D_BEAM = 84
    PROPERTY_1D_ROD = 85
    PROPERTY_1D_PLOT = 86
    PROPERTY_2D_SHELL = 87
    PROPERTY_2D_COMPOSITE_SHELL = 88
    PROPERTY_3D_SOLID = 89
    PROPERTY_3D_GASKET = 90
    PROPERTY_3D_COHESIVE = 91
    PROPERTY_3D_WELDBEAD = 92
    SECTION_GENERAL = 93
    SECTION_LIBRARY = 94
    SECTION_SKETCHER = 95
    CONNECT_MPC = 96
    CONNECT_SPRING = 97
    CONNECT_RBE2 = 98
    CONNECT_CONM = 99
    CONNECT_PROD = 100
    CONNECT_RBAR = 101
    CONNECT_RBE3 = 102
    CONNECT_BUSH = 103
    CONNECT_MOMENT = 104
    CONNECT_WELD = 105
    CONNECT_DAMPER = 106
    CONNECT_CONNECTOR = 107
    CONTACT_ADVC = 108
    CONTACT_NXNASTRAN = 109
    CONTACT_MSCNASTRAN = 110
    CONTACT_ABAQUS = 111
    CONTACT_ANSYS = 112
    CONTACT = 113
    CUSTOM_ATTR_STRING = 114
    CUSTOM_ATTR_VECTOR = 115
    CUSTOM_ATTR_DOUBLE = 116
    DCS = 117
    ADVCPROCESS = 118
    ADVCPROCESS_STATIC = 119
    ADVCPROCESS_DYNAMIC = 120
    ADVCPROCESS_EIGEN = 121
    ADVCPROCESS_CREEP = 122
    ADVCPROCESS_DYNAMIC_EXPLICIT = 123
    ADVCPROCESS_FATIGUE = 124
    ADVCPROCESS_MODAL_FREQ_RESP = 125
    ADVCPROCESS_RESP_SPEC = 126
    ADVCPROCESS_RAND_RESP = 127
    ADVCPROCESS_SSH = 128
    ADVCPROCESS_TH = 129
    ADVCJOB = 130
    ABAQSTEPS = 131
    ABAQSTEPS_STRUCT = 132
    ABAQSTEPS_THERMAL = 133
    ABAQSTEPS_STRUCT_STATIC = 134
    ABAQSTEPS_STRUCT_FREQUENCY = 135
    ABAQSTEPS_STRUCT_COUPLEDTD = 136
    ABAQSTEPS_STRUCT_DYNAMIC = 137
    ABAQSTEPS_STRUCT_DYNAMIC_COUPLEDTD = 138
    ABAQSTEPS_STRUCT_DYNAMIC_EXPLICIT = 139
    ABAQSTEPS_STRUCT_STATICRISK = 140
    ABAQSTEPS_THERMAL_SS = 141
    ABAQSTEPS_THERMAL_TRANSIENT = 142
    ABAQUSJOB = 143
    LBC_MAPPING_HEATFLUX = 144
    CONNECT_GAP = 145
    ANSYSJOB = 146
    NASTRANJOB = 147
    DYANAMISJOB = 148
    WELDORDER = 149
    ATTRIBUTE_FXWELD = 150
    ACTRANJOB = 151
    LSDYNAJOB = 152
    NCS = 153
    ATTRIBUTE_PS_BLENDSURFACE = 154
    LBC_DOFSET = 155
    BEAM_PROP_ATTR = 156
    BEAM_PROP_ATTR2 = 157
    SHELL_PROP_ATTR = 158
    CONN_PROP_ATTR = 159
    LBC_PRETENSION_NXN = 160
    LBC_MAPPING_TEMP_MARINE_ENGINE = 161
    USER_PROP = 162
    CONNECTION_ELEMENT = 163
    CONTACT_TSSS = 164
    LBC_MAPPING_FORCEDDISPLACEMENT = 165
    LBC_MAPPING_FORCED_TEMP = 166
    NASTRAN_POSTJOB = 167
    ADVC2_POSTJOB = 168
    LBC_MAPPING_TEMP_INIT = 174
    POST_NODE = 182
    POST_ELEM = 183
    END = 184
    
class MsgBoxType:
    values = "JPT.MsgBoxType.values"
    MB_WARNING_YESNOCANCEL = 0
    MB_WARNING_YESNO = 1
    MB_WARNING_OK = 2
    MB_WARNING_OKCANCEL = 3
    MB_INFORMATION_YESNOCANCEL = 4
    MB_INFORMATION_YESNO = 5
    MB_INFORMATION_OK = 6
    MB_INFORMATION_OKCANCEL = 7
    MB_CRITICAL_OK = 8
    
class PathType:
    values = "JPT.PathType.values"
    PROGRAM_PATH = 0
    TEMP_PATH = 1
    APPDATA_PATH = 2
    DOC_PATH = 3
    MATERIAL_LIB_FILE_PATH = 4
    MATERIAL_USER_FILE_PATH = 5
    DATABASE_PATH = 6
    SUNSHINE_PATH = 7
    IDE_DATA_PATH = 8
    FILE_PATH = 9
    PSJ_COMMAND_PATH = 10
    
class SelectMethodType:
    values = "JPT.SelectMethodType.values"
    SELMTD_NONE = 0
    SELMTD_BODY = 1
    SELMTD_BAR_BODY = 2
    SELMTD_FACE = 3
    SELMTD_EDGE = 4
    SELMTD_VERTEX = 5
    SELMTD_SOLIDELEM = 6
    SELMTD_ELEM = 7
    SELMTD_ELEM1D = 8
    SELMTD_ELEM_EDGE = 9
    SELMTD_NODE = 10
    SELMTD_CONDITION = 11
    SELMTD_COORDINATE = 12
    SELMTD_GROUP = 13
    SELMTD_PROPERTY = 14
    SELMTD_FACE_POINT = 15
    SELMTD_EDGE_POINT = 16
    SELMTD_VIEW_ITEM = 17
    SELMTD_CONDITION_MPC = 18
    SELMTD_CONDITION_RBE2 = 19
    SELMTD_CONDITION_RBE3 = 20
    SELMTD_CONDITION_RBAR = 21
    SELMTD_CONDITION_SPRING = 22
    SELMTD_CONDITION_MASS = 23
    SELMTD_CONDITION_CONNECTOR = 24
    SELMTD_CONDITION_PRESSURE = 25
    SELMTD_CONDITION_FORCE = 26
    SELMTD_CONDITION_ENFORCE = 27
    SELMTD_CONDITION_CONSTRAIN = 28
    SELMTD_CONDITION_TEMP = 29
    SELMTD_SOLID_TET4 = 30
    SELMTD_SOLID_TET10 = 31
    SELMTD_SOLID_HEX8 = 32
    SELMTD_SOLID_HEX20 = 33
    SELMTD_SOLID_PENT6 = 34
    SELMTD_SOLID_PEN15 = 35
    SELMTD_SOLID_PYRD5 = 36
    SELMTD_SOLID_PYR13 = 37
    SELMTD_SHELL_TRI3 = 38
    SELMTD_SHELL_TRI6 = 39
    SELMTD_SHELL_QUAD4 = 40
    SELMTD_SHELL_QUAD8 = 41
    
class UnitType:
    values = "JPT.UnitType.values"
    Unit_Length = 0
    Unit_Time = 1
    Unit_Mass = 2
    Unit_Force = 3
    Unit_Angle = 4
    Unit_Temperature = 5
    Unit_Area = 6
    Unit_Volume = 7
    Unit_Velocity = 8
    Unit_Acceleration = 9
    Unit_RotateVelo = 10
    Unit_RotateAcc = 11
    Unit_Moment = 12
    Unit_Pressure = 13
    Unit_Density = 14
    Unit_Stiffness = 15
    Unit_RotateStiff = 16
    Unit_DampingCoef = 17
    Unit_RotateDampingCoef = 18
    Unit_Modulus = 19
    Unit_Energy = 20
    Unit_Power = 21
    Unit_ThermalExCoef = 22
    Unit_ThermalConductivity = 23
    Unit_ConvectionCoef = 24
    Unit_SpecificHeat = 25
    Unit_HeatFlux = 26
    Unit_HeatGeneration = 27
    Unit_LinearDensity = 28
    Unit_SurfaceDensity = 29
    Unit_AreaMomentInertia = 30
    Unit_TorsionalConst = 31
    Unit_WarpCoef = 32
    Unit_LinearMassMomentIntertia = 33
    Unit_MomentInertia = 34
    Unit_Stress = 35
    Unit_Strain = 36
    Unit_StrainEnergy = 37
    Unit_ThermalEnergy = 38
    Unit_Frequency = 39
    Unit_VolumeEnergyDensity = 40
    Unit_ElectricalResistivity = 41
    Unit_StressReciprocal = 42
    Unit_ThermalRadiation = 43
    Unit_Displacement = 44
    Unit_EnergyDensity = 45
    Unit_TemperatureGradient = 46
    Unit_Current = 47
    Unit_Voltage = 48
    Unit_ExternalCurrentDensity = 49
    Unit_ElectricalConductivity = 50
    Unit_ElectromagneticBC = 51
    Unit_SurfaceCurrentDensity = 52
    Unit_Charge = 53
    Unit_SurfaceChargeDensity = 54
    Unit_VolumeChargeDensity = 55
    Unit_VolumeCurrentDensity = 56
    Unit_MagneticFluxDensity = 57
    
class JPT:
    AssociateType = AssociateType()
    BoolType = BoolType()
    DItemType = DItemType()
    DTableType = DTableType()
    ElemKind = ElemKind()
    ElemType = ElemType()
    EntityType = EntityType()
    MsgBoxType = MsgBoxType()
    PathType = PathType()
    SelectMethodType = SelectMethodType()
    UnitType = UnitType()
    def DItem():
        return "JPT.DItem()"

    def DFace():
        return "JPT.DFace()"

    def DBody():
        return "JPT.DBody()"

    def DEdge():
        return "JPT.DEdge()"

    def DElem():
        return "JPT.DElem()"

    def DGroup():
        return "JPT.DGroup()"

    def DNode():
        return "JPT.DNode()"

    def VersionInfo():
        return "JPT.VersionInfo()"

    def TVector3d():
        return "JPT.TVector3d()"

    def DItemVector():
        return "JPT.DItemVector()"

    def BodyVector():
        return "JPT.BodyVector()"

    def FaceVector():
        return "JPT.FaceVector()"

    def ElemVector():
        return "JPT.ElemVector()"

    def GroupVector():
        return "JPT.GroupVector()"

    def NodeVector():
        return "JPT.NodeVector()"

    def EdgeVector():
        return "JPT.EdgeVector()"

    def DItemPairVector():
        return "JPT.DItemPairVector()"

    def BeginDatabaseTransaction(transactionName):
        r"""
        ## Description
        
        Disable screen animation, screen update, and status bar update information to improve Jupiter's performance.
        
        :::important
        [JPT.EndDatabaseTransaction()](JPT.EndDatabaseTransaction) should be used at the end of the process, to return Jupiter to the normal state.
        :::
        
        ## Syntax
        
        ```psj
        JPT.BeginDatabaseTransaction("transactionName")
        ```
        
        ## Inputs
        
        ### `transactionName`
        
        - A _String_ specifying the transaction name (used to display the command name in Undo/Redo menu).
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {2}
        # Begin Data Base Transaction
        JPT.BeginDatabaseTransaction("Make meshed model")
        
        # From now on, all the steps inside will be stored as one step - "Make meshed model".
        # You can check it by clicking on the Undo button after the execution process is finished.
        
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                           strName="Cube_2",
                           iPartColor=6409934)
        Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0],
                           strName="Cube_3",
                           iPartColor=13259210)
        Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0],
                           strName="Cube_4",
                           iPartColor=7697908)
        Geometry.Part.Cube(dlOrigin=[0.04, 0.0, 0.0],
                           strName="Cube_5",
                           iPartColor=7463537)
        Geometry.Part.Cube(dlOrigin=[0.05, 0.0, 0.0],
                           strName="Cube_6",
                           iPartColor=7434735)
        Geometry.Part.Cube(dlOrigin=[0.06, 0.0, 0.0],
                           strName="Cube_7",
                           iPartColor=14903267)
        Geometry.Part.Cube(dlOrigin=[0.07, 0.0, 0.0],
                           strName="Cube_8",
                           iPartColor=15658599)
        
        Meshing.SetMeshAttribute(crlParts=[Part(5, 6, 7, 8)],
                                 surfaceMesh=SURFACE_MESH(dGeomAngle=0.7853981634,
                                                          iPerformanceMode=1,
                                                          dAutoMergeTinyFacesAngle=0.5235987756,
                                                          bOutputQuadMesh=True,
                                                          bGeomApprox=True,
                                                          iNextEntityOffsetId=0))
        Meshing.SurfaceMeshing(crlParts=[Part(5, 6, 7, 8)],
                               surfaceMesh=SURFACE_MESH(dGeomAngle=0.7853981634,
                                                        iPerformanceMode=1,
                                                        dAutoMergeTinyFacesAngle=0.5235987756,
                                                        bOutputQuadMesh=True,
                                                        bGeomApprox=True,
                                                        iNextEntityOffsetId=0),
                                                        iThreadNum=12)
        MeshEdit.SurfaceMesh(crlParts=[Part(2, 4, 8, 6)])
        Meshing.SolidMeshing(crlParts=[Part(8, 4, 7, 3)],
                             dGradingFactor=1.05,
                             dStretchLimit=0.1,
                             iSpeedVsQual=1,
                             iRegion=1,
                             bSafeMode=False,
                             iParallel=12,
                             bInternalMeshOnly=False,
                             iPartColor=65280)
        Meshing.SolidMeshing(crlParts=[Part(4)],
                             bTet10=True,
                             dGradingFactor=1.05,
                             dStretchLimit=0.1,
                             iSpeedVsQual=1,
                             iRegion=1,
                             bSafeMode=False,
                             iParallel=12,
                             bInternalMeshOnly=False,
                             iPartColor=65280)
        
        del_faces = [208, 182, 178, 204, 206, 177, 203, 179, 205, 180]
        extrude_faces = [207, 181]
        
        Geometry.DeleteEntity.Face(crlFaces=[Face(*del_faces)])
        
        HexModeling.Linear(crlFaces=[Face(*extrude_faces)],
                           dLength=0.01,
                           iLayer=2,
                           vecSweepDirection=[0.0,
                                              0.0,
                                              1.0],
                           iLinearMethod=4)
        
        MeshEdit.SolidMesh(crlParts=[Part(8)])
        
        # End Data Base Transaction
        JPT.EndDatabaseTransaction()
        ```
        
        """
        message = "JPT.BeginDatabaseTransaction({})".format(transactionName)
        return JPT_RUN_LINE(message)

    def CastDItemToDBody(DItemObject):
        r"""
        ## Description
        
        Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_ object to get the information of the selected body.
        
        ## Syntax
        
        ```psj
        JPT.CastDItemToDBody(DItemObject)
        ```
        
        ## Inputs
        
        ### `DItemObject`
        
        - A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be used to convert.
        - This is a required input.
        
        ## Return Code
        
        A _[DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_ object (Part with relating information).
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model
        Geometry.Part.Cube()
        JPT.ViewFitToModel()
        
        # Get Part object as DItem object from the created list of DItem objects
        listDItemParts = JPT.GetAllByTypeID(JPT.DItemType.BODY)
        dItemPart = listDItemParts[0]
        JPT.Debugger(dItemPart)
        
        # Convert from the above DItem object to DBody object
        dBodyPart = JPT.CastDItemToDBody(dItemPart)
        JPT.Debugger(dBodyPart)
        ```
        
        """
        message = "JPT.CastDItemToDBody({})".format(DItemObject)
        return JPT_RUN_LINE(message)

    def CastDItemToDConnect(DItemObject):
        r"""
        ## Description
        
        Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DConnect](../data-type/psj-utility/pre-utility/built-in-types/DConnect)_ object to get the information of the selected coordinate system.
        
        ## Syntax
        
        ```psj
        JPT.CastDItemToDConnect(DItemObject)
        ```
        
        ## Inputs
        
        ### `DItemObject`
        
        - A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be used to convert.
        - This is a required input.
        
        ## Return Code
        
        A _[DConnect](../data-type/psj-utility/pre-utility/built-in-types/DConnect)_ object (Connection with relating information).
        
        ## Sample Code
        
        ```psj {24}
        # Prepare model
        Geometry.Part.Cube(iPartColor=13290083)
        Geometry.Part.Cube(dlOrigin=[0.012, 0.0, 0.0], strName="Cube_2", iPartColor=6149981)
        Geometry.Part.Cube(dlOrigin=[0.024, 0.0, 0.0], strName="Cube_3", iPartColor=7664244)
        Geometry.Part.Cube(dlOrigin=[0.036, 0.0, 0.0], strName="Cube_4", iPartColor=13588687)
        Geometry.Part.Cube(dlOrigin=[0.036, 0.012, 0.0], strName="Cube_5", iPartColor=14048091)
        Geometry.Part.Cube(dlOrigin=[0.024, 0.012, 0.0], strName="Cube_6", iPartColor=7138156)
        Geometry.Part.Cube(dlOrigin=[0.012, 0.012, 0.0], strName="Cube_7", iPartColor=5489235)
        Geometry.Part.Cube(dlOrigin=[0.0, 0.012, 0.0], strName="Cube_8", iPartColor=7632109)
        Connections.MPC.General.NodesToNodes(crlMasterNodes=[Node(1932)], crlSlaveNodes=[Node(1429)], listMpcConnection=[MPC_CONNECTION(iDof=1), MPC_CONNECTION(iDof=2), MPC_CONNECTION(iDof=4), MPC_CONNECTION(), MPC_CONNECTION(), MPC_CONNECTION()], bUpdateDispCS=1)
        Connections.RigidElements.RBE2.OneToOne(crlMasterTargets=[Node(940)], crlSlaveTargets=[Node(3363)])
        Connections.RigidElements.RBE3.OneToMany(crlMasterTargets=[Node(459, 3889, 3859)], crlSlaveTargets=[Node(3879)], listRbe3TermConnection=[(0, 63, 1), (1, 7, 3)], strName="RBE3_1")
        Connections.SpringsDampers.Spring.OneToOne.sameDoFs(iMethod=17, strName="Spring_2", crlMasterTargets=[Node(2396)], crlSlaveTargets=[Node(2428)], iSpringType=2, posTStiffness=[1.7976931e+308, 1.7976931e+308, 1.7976931e+308], posRStiffness=[1.7976931e+308, 1.7976931e+308, 1.7976931e+308])
        Connections.SpringsDampers.Bush.TwoNodes(crlMaster=[Node(2884)], crlSlave=[Node(2900)], iOriMode=1, dlVector=[0, 0, 0], dlStiffness=[DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL], dlDampCoef=[DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL], dlDampConst=[DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL])
        Connections.SpringsDampers.Damper.AnyEntities11DoFS(iMethod=17, strName="Damper_1", crlMasterTargets=[Node(3382)], crlSlaveTargets=[Node(3398)])
        JPT.ViewFitToModel()
        
        # Get RBE2 Connection object as DItem object from the created list of DItem objects
        listDItemConnections = JPT.GetAllByTypeID(JPT.DItemType.CONNECT_RBE2)
        dItemConnection = listDItemConnections[0]
        JPT.Debugger(dItemConnection)
        
        # Convert from the above DItem object to DConnect object
        dConnection = JPT.CastDItemToDConnect(dItemConnection)
        JPT.Debugger(dConnection)
        ```
        
        """
        message = "JPT.CastDItemToDConnect({})".format(DItemObject)
        return JPT_RUN_LINE(message)

    def CastDItemToDCoord(DItemObject):
        r"""
        ## Description
        
        Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DCoord](../data-type/psj-utility/pre-utility/built-in-types/DCoord)_ object to get the information of the selected coordinate system.
        
        ## Syntax
        
        ```psj
        JPT.CastDItemToDCoord(DItemObject)
        ```
        
        ## Inputs
        
        ### `DItemObject`
        
        - A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be used to convert.
        - This is a required input.
        
        ## Return Code
        
        A _[DCoord](../data-type/psj-utility/pre-utility/built-in-types/DCoord)_ object (Coordinate system with relating information).
        
        ## Sample Code
        
        ```psj {16}
        # Prepare model
        Geometry.Part.Cube(iPartColor=6118844)
        Tools.Coordinates.ThreeNode(crlNodes=[Node(454, 461, 462)])
        Tools.Coordinates.ThreeNode(strName="CRect2", crlNodes=[Node(428, 436, 430)])
        Tools.Coordinates.ThreeNode(strName="CCyl1", iCoordType=1, crlNodes=[Node(457, 474, 473)])
        Tools.Coordinates.ThreeNode(strName="CSph1", iCoordType=2, crlNodes=[Node(316, 340, 333)])
        Tools.Coordinates.ThreeNode(strName="CSph2", iCoordType=2, iOrder=3, crlNodes=[Node(190, 216, 204)])
        JPT.ViewFitToModel()
        
        # Get Coordinate object as DItem object from the created list of DItem objects
        listDItemCoords = JPT.GetAllByTypeID(JPT.DItemType.COORD)
        dItemCoord = listDItemCoords[0]
        JPT.Debugger(dItemCoord)
        
        # Convert from the above DItem object to DCoord object
        dCoord = JPT.CastDItemToDCoord(dItemCoord)
        JPT.Debugger(dCoord)
        ```
        
        """
        message = "JPT.CastDItemToDCoord({})".format(DItemObject)
        return JPT_RUN_LINE(message)

    def CastDItemToDEdge(DItemObject):
        r"""
        ## Description
        
        Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DEdge](../data-type/psj-utility/pre-utility/built-in-types/DEdge)_ object to get the information of the selected edge.
        
        ## Syntax
        
        ```psj
        JPT.CastDItemToDEdge(DItemObject)
        ```
        
        ## Inputs
        
        ### `DItemObject`
        
        - A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be used to convert.
        - This is a required input.
        
        ## Return Code
        
        A _[DEdge](../data-type/psj-utility/pre-utility/built-in-types/DEdge)_ object (Edge with relating information).
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model
        Geometry.Part.Cube()
        JPT.ViewFitToModel()
        
        # Get Edge object as DItem object from the created list of DItem objects
        listDItemEdges = JPT.GetAllByTypeID(JPT.DItemType.EDGE)
        dItemEdge = listDItemEdges[0]
        JPT.Debugger(dItemEdge)
        
        # Convert from the above DItem object to DEdge object
        dEdge = JPT.CastDItemToDEdge(dItemEdge)
        JPT.Debugger(dEdge)
        ```
        
        """
        message = "JPT.CastDItemToDEdge({})".format(DItemObject)
        return JPT_RUN_LINE(message)

    def CastDItemToDElem(DItemObject):
        r"""
        ## Description
        
        Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DElem](../data-type/psj-utility/pre-utility/built-in-types/DElem)_ object to get the information of the selected element.
        
        ## Syntax
        
        ```psj
        JPT.CastDItemToDElem(DItemObject)
        ```
        
        ## Inputs
        
        ### `DItemObject`
        
        - A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be used to convert.
        - This is a required input.
        
        ## Return Code
        
        A _[DElem](../data-type/psj-utility/pre-utility/built-in-types/DElem)_ object (Element with relating information).
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model
        Geometry.Part.Cube()
        JPT.ViewFitToModel()
        
        # Get Element object as DItem object from the created list of DItem objects
        listDItemElems = JPT.GetAllByTypeID(JPT.DItemType.ELEM)
        dItemElem = listDItemElems[0]
        JPT.Debugger(dItemElem)
        
        # Convert from the above DItem object to DElem object
        dElem = JPT.CastDItemToDElem(dItemElem)
        JPT.Debugger(dElem)
        ```
        
        """
        message = "JPT.CastDItemToDElem({})".format(DItemObject)
        return JPT_RUN_LINE(message)

    def CastDItemToDFace(DItemObject):
        r"""
        ## Description
        
        Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DFace](../data-type/psj-utility/pre-utility/built-in-types/DFace)_ object to get the information of the selected (Inputted) face(s).
        
        ## Syntax
        
        ```psj
        JPT.CastDItemToDFace(DItemObject)
        ```
        
        ## Inputs
        
        ### `DItemObject`
        
        - A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be used to convert.
        - This is a required input.
        
        ## Return Code
        
        A _[DFace](../data-type/psj-utility/pre-utility/built-in-types/DFace)_ object (Face with relating information).
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model
        Geometry.Part.Cube()
        JPT.ViewFitToModel()
        
        # Get Face object as DItem object from the created list of DItem objects
        listDItemFaces = JPT.GetAllByTypeID(JPT.DItemType.FACE)
        dItemFace = listDItemFaces[0]
        JPT.Debugger(dItemFace)
        
        # Convert from the above DItem object to DFace object
        dFace = JPT.CastDItemToDFace(dItemFace)
        JPT.Debugger(dFace)
        ```
        
        """
        message = "JPT.CastDItemToDFace({})".format(DItemObject)
        return JPT_RUN_LINE(message)

    def CastDItemToDGroup(DItemObject):
        r"""
        ## Description
        
        Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DGroup](../data-type/psj-utility/pre-utility/built-in-types/DGroup)_ object to get the information of the selected group.
        
        ## Syntax
        
        ```psj
        JPT.CastDItemToDGroup(DItemObject)
        ```
        
        ## Inputs
        
        ### `DItemObject`
        
        - A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be used to convert.
        - This is a required input.
        
        ## Return Code
        
        A _[DGroup](../data-type/psj-utility/pre-utility/built-in-types/DGroup)_ object (Group with relating information).
        
        ## Sample Code
        
        ```psj {12}
        # Prepare model
        Geometry.Part.Cube()
        Tools.Group.CreateGroup(strGroupName="Group1", crlTargets=[Face(26)])
        JPT.ViewFitToModel()
        
        # Get Group object as DItem object from the created list of DItem objects
        listDItemGroups = JPT.GetAllByTypeID(JPT.DItemType.GROUP)
        dItemGroup = listDItemGroups[0]
        JPT.Debugger(dItemGroup)
        
        # Convert from the above DItem object to DGroup object
        dGroup = JPT.CastDItemToDGroup(dItemGroup)
        JPT.Debugger(dGroup)
        ```
        
        """
        message = "JPT.CastDItemToDGroup({})".format(DItemObject)
        return JPT_RUN_LINE(message)

    def CastDItemToDLoadBC(DItemObject):
        r"""
        ## Description
        
        Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DLoadBC](../data-type/psj-utility/pre-utility/built-in-types/DLoadBC)_ object to get the information of the selected coordinate system.
        
        ## Syntax
        
        ```psj
        JPT.CastDItemToDLoadBC(DItemObject)
        ```
        
        ## Inputs
        
        ### `DItemObject`
        
        - A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be used to convert.
        - This is a required input.
        
        ## Return Code
        
        A _[DLoadBC](../data-type/psj-utility/pre-utility/built-in-types/DLoadBC)_ object (Boundary condition with relating information).
        
        ## Sample Code
        
        ```psj {12}
        # Prepare simple sample
        Geometry.Part.Cube(iPartColor=6409934)
        BoundaryConditions.Pressure.General(crlTargets=[Face(26)])
        JPT.ViewFitToModel()
        
        # Get LBC object (Pressure) as DItem object from the created list of DItem objects
        listDItemLoadBCs = JPT.GetAllByTypeID(JPT.DItemType.LBC_G_PRESSURE)
        dItemLoadBC = listDItemLoadBCs[0]
        JPT.Debugger(dItemLoadBC)
        
        # Convert from the above DItem object to DLoadBC object
        dLoadBC = JPT.CastDItemToDLoadBC(dItemLoadBC)
        JPT.Debugger(dLoadBC)
        ```
        
        """
        message = "JPT.CastDItemToDLoadBC({})".format(DItemObject)
        return JPT_RUN_LINE(message)

    def CastDItemToDNode(DItemObject):
        r"""
        ## Description
        
        Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DNode](../data-type/psj-utility/pre-utility/built-in-types/DNode)_ object to get the information of the selected node.
        
        ## Syntax
        
        ```psj
        JPT.CastDItemToDNode(DItemObject)
        ```
        
        ## Inputs
        
        ### `DItemObject`
        
        - A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be used to convert.
        - This is a required input.
        
        ## Return Code
        
        A _[DNode](../data-type/psj-utility/pre-utility/built-in-types/DNode)_ object (Node with relating information).
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model
        Geometry.Part.Cube()
        JPT.ViewFitToModel()
        
        # Get LBC object (Pressure) as DItem object from the created list of DItem objects
        listDItemNodes = JPT.GetAllByTypeID(JPT.DItemType.NODE)
        dItemNode = listDItemNodes[0]
        JPT.Debugger(dItemNode)
        
        # Convert from the above DItem object to DNode object
        dNode = JPT.CastDItemToDNode(dItemNode)
        JPT.Debugger(dNode)
        ```
        
        """
        message = "JPT.CastDItemToDNode({})".format(DItemObject)
        return JPT_RUN_LINE(message)

    def CastDItemToDROElem(DItemObject):
        r"""
        ## Description
        
        Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DPostElem](../data-type/psj-utility/post-utility/post-built-in-types/DPostElem)_ object to get the information of the selected Post element.
        
        ## Syntax
        
        ```psj
        JPT.CastDItemToDROElem(DItemObject)
        ```
        
        ## Inputs
        
        ### `DItemObject`
        
        - A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be used to convert.
        - This is a required input.
        
        ## Return Code
        
        A _[DPostElem](../data-type/psj-utility/post-utility/post-built-in-types/DPostElem)_ object (Post element with relating information).
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        # Get Element object as DItem object from the created list of DItem objects
        listDItemPostElems = JPT.GetAllByTypeID(JPT.DItemType.POST_ELEM)
        dItemPostElem = listDItemPostElems[0]
        JPT.Debugger(dItemPostElem)
        
        # Convert from the above DItem object to DElem object
        dPostElem = JPT.CastDItemToDROElem(dItemPostElem)
        JPT.Debugger(dPostElem)
        ```
        
        """
        message = "JPT.CastDItemToDROElem({})".format(DItemObject)
        return JPT_RUN_LINE(message)

    def CastDItemToDRONode(DItemObject):
        r"""
        ## Description
        
        Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DPostNode](../data-type/psj-utility/post-utility/post-built-in-types/DPostNode)_ object to get the information of the selected Post node.
        
        ## Syntax
        
        ```psj
        JPT.CastDItemToDRONode(DItemObject)
        ```
        
        ## Inputs
        
        ### `DItemObject`
        
        - A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be used to convert.
        - This is a required input.
        
        ## Return Code
        
        A _[DPostNode](../data-type/psj-utility/post-utility/post-built-in-types/DPostNode)_ object (Post node with relating information).
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        # Get LBC object (Pressure) as DItem object from the created list of DItem objects
        listDItemPostNodes = JPT.GetAllByTypeID(JPT.DItemType.POST_NODE)
        dItemPostNode = listDItemPostNodes[0]
        JPT.Debugger(dItemPostNode)
        
        # Convert from the above DItem object to DPostNode object
        dPostNode = JPT.CastDItemToDRONode(dItemPostNode)
        JPT.Debugger(dPostNode)
        ```
        
        """
        message = "JPT.CastDItemToDRONode({})".format(DItemObject)
        return JPT_RUN_LINE(message)

    def CastDItemToDSubGroup(DItemObject):
        r"""
        ## Description
        
        Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DSubGroup](../data-type/psj-utility/pre-utility/built-in-types/DSubGroup)_ object to get the information of the selected group.
        
        ## Syntax
        
        ```psj
        JPT.CastDItemToDSubGroup(DItemObject)
        ```
        
        ## Inputs
        
        ### `DItemObject`
        
        - A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be used to convert.
        - This is a required input.
        
        ## Return Code
        
        A _[DSubGroup](../data-type/psj-utility/pre-utility/built-in-types/DSubGroup)_ object (SubGroup with relating information).
        
        ## Sample Code
        
        ```psj {24}
        # Prepare model
        Geometry.Part.Cube(iPartColor=7697908)
        
        Geometry.Part.Cube(
            dlOrigin=[0.01, 0.0, 0.0], 
            strName="Cube_2", 
            iPartColor=14903267)
        
        mating_faces=Assemble.FindMatingFaceEx(
            crlTaBodies=[Part(1, 2)], 
            dMatingTol=0.000222222)
        
        Assemble.AssembleFaceEx(
            ilPairFaceToMakeShareFace=mating_faces, 
            dTolerance=0.000222222, 
            iTypeConnectPos=0)
        
        # Get Sub Group object as DItem object from the created list of DItem objects
        listDItemSubGroups = JPT.GetAllByTypeID(JPT.DItemType.SUP_GROUP)
        dItemSubGroup = listDItemSubGroups[0]
        JPT.Debugger(dItemSubGroup)
        
        # Convert from the above DItem object to DGroup object
        dSubGroup = JPT.CastDItemToDSubGroup(dItemSubGroup)
        JPT.Debugger(dSubGroup)
        ```
        
        """
        message = "JPT.CastDItemToDSubGroup({})".format(DItemObject)
        return JPT_RUN_LINE(message)

    def CastToDItem(Object):
        r"""
        ## Description
        
        Convert the selected object to _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to get all the related information.
        
        ## Syntax
        
        ```psj
        JPT.CastToDItem(Object)
        ```
        
        ## Inputs
        
        ### `Object`
        
        - An _Object_ in Jupiter such as _[DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_, _[DFace](../data-type/psj-utility/pre-utility/built-in-types/DFace)_, _[DElem](../data-type/psj-utility/pre-utility/built-in-types/DElem)_, _[DEdge](../data-type/psj-utility/pre-utility/built-in-types/DEdge)_, _[DGroup](../data-type/psj-utility/pre-utility/built-in-types/DGroup)_, _[DNode](../data-type/psj-utility/pre-utility/built-in-types/DNode)_, etc.
        - This is a required input.
        
        ## Return Code
        
        A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object (Base object with all the information).
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model
        Geometry.Part.Cube()
        JPT.ViewFitToModel()
        
        # Get Part object as DBody object from the created list of DBody objects
        listDBodyParts = JPT.GetAllParts()
        dBodyPart = listDBodyParts[0]
        JPT.Debugger(dBodyPart)
        
        # Convert from the above DBody object to DItem object
        dItemPart = JPT.CastToDItem(dBodyPart)
        JPT.Debugger(dItemPart)
        ```
        
        """
        message = "JPT.CastToDItem({})".format(Object)
        return JPT_RUN_LINE(message)

    def CheckLicense(Feature):
        r"""
        ## Description
        
        Check whether the inputted license is activated or not.
        
        ## Syntax
        
        ```psj
        JPT.CheckLicense("Feature")
        ```
        
        ## Inputs
        
        ### `Feature`
        
        - A _String_ specifying the Jupiter license's name.
        - The Jupiter license's name can be found at <menuselection>Home &#187; Preference &#187; License</menuselection>.
        - This is a required input.
        
        ## Return Code
        
        A _Boolean_ specifying the status of license:
        
        - _True_: License feature is activated.
        - _False_: License feature is deactivated.
        
        ## Sample Code
        
        ```psj {2}
        # Get the status of the JPT_BASE feature license and print to the screen
        lic = JPT.CheckLicense("JPT_BASE")
        print(lic)
        ```
        
        """
        message = "JPT.CheckLicense({})".format(Feature)
        return JPT_RUN_LINE(message)

    def ClearAllSelection():
        r"""
        ## Description
        
        Clear all the selected entities.
        
        ## Syntax
        
        ```psj
        JPT.ClearAllSelection()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {10}
        # Prepare model
        Geometry.Part.Cube(iPartColor=6974164)
        Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=7599987)
        JPT.ViewFitToModel()
        
        # Select face with ID = 51
        JPT.SelectionByID(JPT.DItemType.FACE, 51, True)
        
        # Deselect all the selected entities
        JPT.ClearAllSelection()
        ```
        
        """
        message = "JPT.ClearAllSelection({})".format('')
        return JPT_RUN_LINE(message)

    def ClearDraw():
        r"""
        ## Description
        
        Clear all the drawings in Main Window.
        
        ## Syntax
        
        ```psj
        JPT.ClearDraw()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        - A _Boolean_ specifying Succeeded or Failed.
          - True: Succeeded.
          - False: Failed.
        
        ## Sample Code
        
        ```psj {2}
        # Clear all the drawings.
        JPT.ClearDraw()
        ```
        
        """
        message = "JPT.ClearDraw({})".format('')
        return JPT_RUN_LINE(message)

    def ClearLog():
        r"""
        ## Description
        
        Clear all the text existing in the Python API window.
        
        ## Syntax
        
        ```psj
        JPT.ClearLog()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {2}
        # Clear all the text existing on the Python API window
        JPT.ClearLog()
        ```
        
        """
        message = "JPT.ClearLog({})".format('')
        return JPT_RUN_LINE(message)

    def ClearMacroLog():
        r"""
        ## Description
        
        Clear all the text existing in the Macro window.
        
        ## Syntax
        
        ```psj
        JPT.ClearMacroLog()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {2}
        # Clear all the text existing on the Macro window
        JPT.ClearMacroLog()
        ```
        
        """
        message = "JPT.ClearMacroLog({})".format('')
        return JPT_RUN_LINE(message)

    def ClearOutputLog():
        r"""
        ## Description
        
        Clear all the text existing in the Output window.
        
        ## Syntax
        
        ```psj
        JPT.ClearOutputLog()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {2}
        # Clear all the text existing on the Output window
        JPT.ClearOutputLog()
        ```
        
        """
        message = "JPT.ClearOutputLog({})".format('')
        return JPT_RUN_LINE(message)

    def ClearPreview():
        r"""
        ## Description
        
        Clear preview render on the main screen.
        
        ## Syntax
        
        ```psj
        JPT.ClearPreview(...)
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {12}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], strName="Cube_2", iPartColor=13259210)
        JPT.ViewFitToModel()
        
        #Preview:
        color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
        parts = JPT.GetAllParts()
        JPT.PreviewScaling(parts,[2,1.1,1.1],[0,0,0],color,0.2)
        
        #Clear Preview:
        JPT.ClearPreview()
        ```
        
        """
        message = "JPT.ClearPreview({})".format('')
        return JPT_RUN_LINE(message)

    def ClearRedo():
        r"""
        ## Description
        
        Clear all the saved redo steps.
        
        ## Syntax
        
        ```psj
        JPT.ClearRedo()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {2}
        # Clear all the saved redo steps
        JPT.ClearRedo()
        ```
        
        """
        message = "JPT.ClearRedo({})".format('')
        return JPT_RUN_LINE(message)

    def ClearUndo():
        r"""
        ## Description
        
        Clear all the saved undo steps.
        
        ## Syntax
        
        ```psj
        JPT.ClearUndo()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {2}
        # Clear all the saved undo steps
        JPT.ClearUndo()
        ```
        
        """
        message = "JPT.ClearUndo({})".format('')
        return JPT_RUN_LINE(message)

    def CloseAllGraphViews():
        r"""
        ## Description
        
        Close all the graph views (graph windows).
        
        ## Syntax
        
        ```psj
        JPT.CloseAllGraphViews()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {88}
        # Import data and load result
        resultDoc=JPT.GetActiveDocument()
        samplePath1=JPT.GetProgramPath() + '\\SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2'
        Home.ImportResults.Nastran(strPath=samplePath1, dFaceAngle=60.16, dEdgeAngle=60.16)
        Post.ShowContour(crPostJob=TSVPostJob(1), 
                        lContourSettings=[PostContourSetting(
                            postResultKey=PostResultKey(
                                iAnalysisType=1, 
                                iResultSet=1, 
                                iTimeStep=1, 
                                strResultName="Displacement", 
                                strResultCompName="Translational", 
                                iResultPos=1), 
                                postDataOp=PostDataOp(iResultLocation=1, iOptionCoord=1))])
        Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                            postResultKey=PostResultKey(
                                iAnalysisType=1, 
                                iResultSet=1, 
                                iTimeStep=1, 
                                strResultName="Displacement", 
                                strResultCompName="Translational"))
        Post.EnableMiddleNodes()
        JPT.Exec('ViewShowMesh(1)')
        Post.Note.Node(crlTargets=[RONode(60, 72, 60, 112, 114, 127)])
        
        # Create graph in the new graph view.
        Chart.CreateGraph(iNumData=6, 
                        strLineTitle="Nodal value for X Y Plot", 
                        dlAxisDataX=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0], 
                        dlAxisDataY=[0.000737, 0.001655, 0.000694, 0.0, 0.000769, 0.0], 
                        strChartTitle="Nodal value for X Y Plot", 
                        strAxisTitleX="Index", 
                        strAxisTitleY="Data", 
                        bNewChart=False)
        WatchData.Toolbar.DeleteAll(iTabIndex=0)
        
        # Create another graph in the new graph view.
        JPT.SetActiveDocumentByID(resultDoc.docID, 1)
        Post.Note.Node(crlTargets=[RONode(5, 16, 8, 15, 7, 114, 109)])
        Chart.CreateGraph(iNumData=7, 
                        strLineTitle="Nodal value for X Y Plot", 
                        dlAxisDataX=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], 
                        dlAxisDataY=[0.00071, 0.001655, 0.000864, 0.000871, 0.000813, 0.000379, 0.0], 
                        strChartTitle="Nodal value for X Y Plot", 
                        strAxisTitleX="Index", 
                        strAxisTitleY="Data", 
                        bNewChart=False)
        
        # Import another data and load result.
        JPT.CreateNewDocument()
        samplePath2=JPT.GetProgramPath() + '\\SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2'
        Home.ImportResults.Nastran(strPath=samplePath2, dFaceAngle=60.16, dEdgeAngle=60.16)
        Post.ShowContour(crPostJob=TSVPostJob(1), 
                        lContourSettings=[PostContourSetting(
                            postResultKey=PostResultKey(
                                iAnalysisType=2, 
                                iResultSet=1, 
                                iTimeStep=1, 
                                strResultName="Stress", 
                                strResultCompName="YY", 
                                iResultPos=4), 
                            postDataOp=PostDataOp(
                                iResultLocation=1, 
                                iOptionCoord=1, 
                                iOptionConversion=1, 
                                iOptionContinuous=8))])
        Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                            postResultKey=PostResultKey(
                                iAnalysisType=2, 
                                iResultSet=1, 
                                iTimeStep=1, 
                                strResultName="Stress", 
                                strResultCompName="YY"))
        JPT.Exec('ViewShowMesh(1)')
        Post.Note.Node(crlTargets=[RONode(131, 127, 129, 45)])
        
        # Create graph in the new graph view.
        Chart.CreateGraph(iNumData=4, 
                        strLineTitle="Nodal value for X Y Plot", 
                        dlAxisDataX=[1.0, 2.0, 3.0, 4.0], 
                        dlAxisDataY=[-5434540.0, 5421610.0, 3557350.0, 5421610.0], 
                        strChartTitle="Nodal value for X Y Plot", 
                        strAxisTitleX="Index", 
                        strAxisTitleY="Data", 
                        bNewChart=False)
        
        # Close all the graph views.
        JPT.CloseAllGraphViews()
        ```
        
        """
        message = "JPT.CloseAllGraphViews({})".format('')
        return JPT_RUN_LINE(message)

    def CloseDocumentByID(docID):
        r"""
        ## Description
        
        Close indicated document by using its ID.
        
        ## Syntax
        
        ```psj
        JPT.CloseDocumentByID(docID)
        ```
        
        ## Inputs
        
        ### `docID`
        
        - A _String_ specifying the ID of document to be closed.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {6}
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
        JPT.CreateNewDocument()
        for doc in JPT.GetDocumentList():
            if doc.docName == "101_solid":
                JPT.CloseDocumentByID(doc.docID)
        ```
        
        """
        message = "JPT.CloseDocumentByID({})".format(docID)
        return JPT_RUN_LINE(message)

    def CloseDocumentByName(docName):
        r"""
        ## Description
        
        Close indicated document by using its name.
        
        ## Syntax
        
        ```psj
        JPT.CloseDocumentByName(docName)
        ```
        
        ## Inputs
        
        ### `docName`
        
        - A _String_ specifying the name of document to be closed.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {4}
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
        JPT.CreateNewDocument()
        JPT.CloseDocumentByName("101_solid")
        ```
        
        """
        message = "JPT.CloseDocumentByName({})".format(docName)
        return JPT_RUN_LINE(message)

    def CloseGraphViewByDocumentName(documentName):
        r"""
        ## Description
        
        Close all the graph views (graph windows) belongs to indicated document. 
        
        ## Syntax
        
        ```psj
        JPT.CloseGraphViewByDocumentName(...)
        ```
        
        ## Inputs
        
        ### `documentName`
        
        - A value indicates document to close graph views that belongs to.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {88}
        # Import data and load result
        resultDoc=JPT.GetActiveDocument()
        samplePath1=JPT.GetProgramPath() + '\\SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2'
        Home.ImportResults.Nastran(strPath=samplePath1, dFaceAngle=60.16, dEdgeAngle=60.16)
        Post.ShowContour(crPostJob=TSVPostJob(1), 
                        lContourSettings=[PostContourSetting(
                            postResultKey=PostResultKey(
                                iAnalysisType=1, 
                                iResultSet=1, 
                                iTimeStep=1, 
                                strResultName="Displacement", 
                                strResultCompName="Translational", 
                                iResultPos=1), 
                                postDataOp=PostDataOp(iResultLocation=1, iOptionCoord=1))])
        Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                            postResultKey=PostResultKey(
                                iAnalysisType=1, 
                                iResultSet=1, 
                                iTimeStep=1, 
                                strResultName="Displacement", 
                                strResultCompName="Translational"))
        Post.EnableMiddleNodes()
        JPT.Exec('ViewShowMesh(1)')
        Post.Note.Node(crlTargets=[RONode(60, 72, 60, 112, 114, 127)])
        
        # Create graph in the new graph view.
        Chart.CreateGraph(iNumData=6, 
                        strLineTitle="Nodal value for X Y Plot", 
                        dlAxisDataX=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0], 
                        dlAxisDataY=[0.000737, 0.001655, 0.000694, 0.0, 0.000769, 0.0], 
                        strChartTitle="Nodal value for X Y Plot", 
                        strAxisTitleX="Index", 
                        strAxisTitleY="Data", 
                        bNewChart=False)
        WatchData.Toolbar.DeleteAll(iTabIndex=0)
        
        # Create another graph in the new graph view.
        JPT.SetActiveDocumentByID(resultDoc.docID, 1)
        Post.Note.Node(crlTargets=[RONode(5, 16, 8, 15, 7, 114, 109)])
        Chart.CreateGraph(iNumData=7, 
                        strLineTitle="Nodal value for X Y Plot", 
                        dlAxisDataX=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], 
                        dlAxisDataY=[0.00071, 0.001655, 0.000864, 0.000871, 0.000813, 0.000379, 0.0], 
                        strChartTitle="Nodal value for X Y Plot", 
                        strAxisTitleX="Index", 
                        strAxisTitleY="Data", 
                        bNewChart=False)
        
        # Import another data and load result.
        JPT.CreateNewDocument()
        samplePath2=JPT.GetProgramPath() + '\\SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2'
        Home.ImportResults.Nastran(strPath=samplePath2, dFaceAngle=60.16, dEdgeAngle=60.16)
        Post.ShowContour(crPostJob=TSVPostJob(1), 
                        lContourSettings=[PostContourSetting(
                            postResultKey=PostResultKey(
                                iAnalysisType=2, 
                                iResultSet=1, 
                                iTimeStep=1, 
                                strResultName="Stress", 
                                strResultCompName="YY", 
                                iResultPos=4), 
                            postDataOp=PostDataOp(
                                iResultLocation=1, 
                                iOptionCoord=1, 
                                iOptionConversion=1, 
                                iOptionContinuous=8))])
        Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                            postResultKey=PostResultKey(
                                iAnalysisType=2, 
                                iResultSet=1, 
                                iTimeStep=1, 
                                strResultName="Stress", 
                                strResultCompName="YY"))
        JPT.Exec('ViewShowMesh(1)')
        Post.Note.Node(crlTargets=[RONode(131, 127, 129, 45)])
        
        # Create graph in the new graph view.
        Chart.CreateGraph(iNumData=4, 
                        strLineTitle="Nodal value for X Y Plot", 
                        dlAxisDataX=[1.0, 2.0, 3.0, 4.0], 
                        dlAxisDataY=[-5434540.0, 5421610.0, 3557350.0, 5421610.0], 
                        strChartTitle="Nodal value for X Y Plot", 
                        strAxisTitleX="Index", 
                        strAxisTitleY="Data", 
                        bNewChart=False)
        
        # Close all the graph views.
        JPT.CloseGraphViewByDocumentName('101_solid')
        
        ```
        
        """
        message = "JPT.CloseGraphViewByDocumentName({})".format(documentName)
        return JPT_RUN_LINE(message)

    def CollapseAssemblyTree():
        r"""
        ## Description
        
        Collapse all the items existing on the Assembly window.
        
        > This utility is used to collapse all the items existing on the Assembly window after using _[JPT.ExpandAssemblyTree()](JPT.ExpandAssemblyTree)_ utility.
        
        ## Syntax
        
        ```psj
        JPT.CollapseAssemblyTree()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {36}
        # Preparing tree
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2", iPartColor=6409934)
        Geometry.Part.Cube(strName="Cube_3", iPartColor=13259210)
        Geometry.Part.Cube(strName="Cube_4", iPartColor=7697908)
        Geometry.Part.Cube(strName="Cube_5", iPartColor=7463537)
        Geometry.Part.Cube(strName="Cube_6", iPartColor=7434735)
        Geometry.Part.Cube(strName="Cube_7", iPartColor=14903267)
        Geometry.Part.Cube(strName="Cube_8", iPartColor=15658599)
        Geometry.Part.Cube(strName="Cube_9", iPartColor=7961077)
        Geometry.Part.Cube(strName="Cube_10", iPartColor=7829501)
        Geometry.Part.Cube(strName="Cube_11", iPartColor=11842649)
        Geometry.Part.Cube(strName="Cube_12", iPartColor=14968422)
        Geometry.Part.Cube(strName="Cube_13", iPartColor=6250447)
        Geometry.Part.Cube(strName="Cube_14", iPartColor=12734402)
        Assembly.RightClick.AddSubAssembly()
        Assembly.RightClick.AddSubAssembly()
        Assembly.RightClick.AddSubAssembly(crInst=Inst(1))
        Assembly.RightClick.AddSubAssembly(crInst=Inst(2))
        Assembly.RightClick.AddSubAssembly(crInst=Inst(4))
        Assembly.RightClick.AddSubAssembly(crInst=Inst(5))
        Assembly.RightClick.AddSubAssembly(crInst=Inst(3))
        Assembly.RightClick.AddSubAssembly(crInst=Inst(6))
        Assembly.RightClick.AddSubAssembly(crInst=Inst(7))
        Assembly.RightClick.AddSubAssembly(crInst=Inst(7))
        Assembly.RightClick.AddSubAssembly(crInst=Inst(7))
        Connections.MPC.General.NodesToNodes(crlMasterNodes=[Node(6425)], crlSlaveNodes=[Node(6776)], listMpcConnection=[MPC_CONNECTION(iDof=1), MPC_CONNECTION(iDof=2), MPC_CONNECTION(iDof=4), MPC_CONNECTION(), MPC_CONNECTION(), MPC_CONNECTION()], bUpdateDispCS=1)
        Connections.MPC.General.NodesToNodes(strName="MPC_2", crlMasterNodes=[Node(6776)], crlSlaveNodes=[Node(6775)], listMpcConnection=[MPC_CONNECTION(iDof=1), MPC_CONNECTION(iDof=2), MPC_CONNECTION(iDof=4), MPC_CONNECTION(), MPC_CONNECTION(), MPC_CONNECTION()], bUpdateDispCS=1)
        Connections.MPC.General.NodesToNodes(strName="MPC_3", crlMasterNodes=[Node(6775)], crlSlaveNodes=[Node(6774)], listMpcConnection=[MPC_CONNECTION(iDof=1), MPC_CONNECTION(iDof=2), MPC_CONNECTION(iDof=4), MPC_CONNECTION(), MPC_CONNECTION(), MPC_CONNECTION()], bUpdateDispCS=1)
        Connections.MPC.General.NodesToNodes(strName="MPC_4", crlMasterNodes=[Node(6774)], crlSlaveNodes=[Node(6773)], listMpcConnection=[MPC_CONNECTION(iDof=1), MPC_CONNECTION(iDof=2), MPC_CONNECTION(iDof=4), MPC_CONNECTION(), MPC_CONNECTION(), MPC_CONNECTION()], bUpdateDispCS=1)
        
        # Expand all the items existing on the Assembly window
        JPT.ExpandAssemblyTree()
        
        # Collapse all the collapsed items existing on the Assembly window
        JPT.CollapseAssemblyTree()
        ```
        
        """
        message = "JPT.CollapseAssemblyTree({})".format('')
        return JPT_RUN_LINE(message)

    def ConvertCoordinateFromGlobalToLocal(DItemType, itemID, DCoord):
        r"""
        ## Description
        
        Convert global coordinate of selected DItem Type into specified local coordinate.
        
        ## Syntax
        
        ```psj
        JPT.ConvertCoordinateFromGlobalToLocal(DItemType, itemID, DCoord)
        ```
        
        ## Inputs
        
        ### `DItemType`
        
        - An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ of BODY, FACE, ELEMENT, EDGE, or NODE entity in Jupiter.
        - This is a required input.
        
        ### `itemID`
        
        - An _Integer_ specifying the ID of the target entity.
        - This is a required input.
        
        ### `DCoord`
        
        - A _[DCoord](../data-type/psj-utility/pre-utility/built-in-types/DCoord)_ object specifying Coordinate System which will be used to convert.
        - This is a required input.
        
        ## Return Code
        
        A _[DItemPair](../data-type/psj-utility/pre-utility/built-in-types/DItemPair)_ object specifying the information of target entity according to the converted Coordinate System.
        - `firstDItem` is an _integer_ specifying the Node IDs of target entity.
        - `secondDItem` is a _[TVector3d](../data-type/psj-utility/pre-utility/built-in-types/TVector3d)_ object specifying the coordinates of the corresponding node according to the converted Coordinate System.
        
        ## Sample Code
        
        ```psj {9}
        # Prepare model and local coordinate
        Geometry.Part.Cube()
        JPT.ViewFitToModel()
        Tools.Coordinates.ThreeNode(crlNodes=[Node(488, 96, 88)])
        
        # Get all local coordinates
        # And convert global coordinate of specified DItemType.NODE into the selected local coordinate
        listCoords = JPT.GetAllCoordinates()
        convertCoord = JPT.ConvertCoordinateFromGlobalToLocal(JPT.DItemType.NODE, 8, listCoords[0])
        
        
        # Get node ID and coordinates of DItem.NODE object according to the converted Coordinate System
        JPT.Debugger(convertCoord[0].first)
        JPT.Debugger(convertCoord[0].second)
        ```
        
        """
        message = "JPT.ConvertCoordinateFromGlobalToLocal({},{},{})".format(DItemType,itemID,DCoord)
        return JPT_RUN_LINE(message)

    def ConvertFromDocUnit(inputValue, unitType):
        r"""
        ## Description
        
        Convert the inputted value from the current using Jupiter unit system to SI\[m\] unit (Jupiter macro unit).
        The return value will be the value after the conversion.
        
        ## Syntax
        
        ```psj
        JPT.ConvertFromDocUnit(inputValue, unitType)
        ```
        
        ## Inputs
        
        ### `inputValue`
        
        - A _Double_ which will be used for converting.
        - This is a required input.
        
        ### `unitType`
        
        - An _Enum_ specifying the _[Unit Types](../data-type/psj-utility/pre-utility/enumeration-types/unit-types.md)_ which will be used as the reference for converting.
        - The type of unit can be found at: <menuselection>Home &#187; Preference &#187; Unit</menuselection> in Jupiter.
        - This is a required input.
        
        ## Return Code
        
        A _Double_ specifying the converted value.
        
        ## Sample Code
        
        ```psj {2}
        # Convert the value = 1 from the current Jupiter Unit system to Jupiter macro unit system
        convertFromDoc = JPT.ConvertFromDocUnit(1, JPT.UnitType.Unit_Length)
        JPT.Debugger(convertFromDoc)
        ```
        
        """
        message = "JPT.ConvertFromDocUnit({},{})".format(inputValue,unitType)
        return JPT_RUN_LINE(message)

    def ConvertFromMacroUnit(inputValue, unitType, outputValueType):
        r"""
        ## Description
        
        Convert the inputted value with the specified unit to the SI\[m\] unit (Jupiter macro unit).
        The return value will be the value after the conversion.
        
        ## Syntax
        
        ```psj
        JPT.ConvertFromMacroUnit(inputValue, unitType, outputValueType)
        ```
        
        ## Inputs
        
        ### `inputValue`
        
        - A _Double_ which will be used for converting.
        - This is a required input.
        
        ### `unitType`
        
        - An _Enum_ specifying the _[Unit Types](../data-type/psj-utility/pre-utility/enumeration-types/unit-types.md)_ which will be used as the reference for converting.
        - The type of unit can be found at: <menuselection>Home &#187; Preference &#187; Unit</menuselection> in Jupiter.
        - This is a required input.
        
        ### `outputValueType`
        
        - A _String_ specifying the indicated unit of the inputted value which will be used for converting to Jupiter macro unit.
        - This is a required input.
        
        ## Return Code
        
        A _Double_ specifying the converted value.
        
        ## Sample Code
        
        ```psj {2}
        # Convert 1mm to the Jupiter macro unit system
        convertFromMacro = JPT.ConvertFromMacroUnit(1, JPT.UnitType.Unit_Length, 'mm') # mm -> m
        JPT.Debugger(convertFromMacro) # 0.001 m
        ```
        
        """
        message = "JPT.ConvertFromMacroUnit({},{},{})".format(inputValue,unitType,outputValueType)
        return JPT_RUN_LINE(message)

    def ConvertJPTColorToRGB(colorValue):
        r"""
        ## Description
        
        Convert color value in Jupiter to a _String_ specifying RGB (Red, Green, Blue) code.
        
        ## Syntax
        
        ```psj
        JPT.ConvertJPTColorToRGB(colorValue)
        ```
        
        ## Inputs
        
        ### `colorValue`
        
        - An _Integer_ specifying the color value in Jupiter.
        - This is a required input.
        
        ## Return Code
        
        A _String_ specifying the converted RGB code with value = RGB(redCode,greenCode,blueCode)
        
        ## Sample Code
        
        ```psj {2}
        # Convert the color code = 255 in Jupiter to RGB color code
        stringRGB = JPT.ConvertJPTColorToRGB(255) # Return RGB(255,0,0)
        # Split the RGB code and store it as Red Green Blue color code
        r, g, b = stringRGB[4:-1].strip().split(",") # String = RGB(255,0,0) -> List = [255, 0, 0]
        print(f"Output value of this function: {stringRGB}")
        print(f"It means: Red = {r} | Green = {g} | Blue = {b}")
        ```
        
        """
        message = "JPT.ConvertJPTColorToRGB({})".format(colorValue)
        return JPT_RUN_LINE(message)

    def ConvertRGBToJPTColor(redValue, greenValue, blueValue):
        r"""
        ## Description
        
        Convert RGB (Red, Green, Blue) color code to color value in Jupiter.
        
        ## Syntax
        
        ```psj
        JPT.ConvertRGBToJPTColor(redValue, greenValue, blueValue)
        ```
        
        ## Inputs
        
        ### `redValue`
        
        - An _Integer_ specifying the red color code.
        - This is a required input.
        
        ### `greenValue`
        
        - An _Integer_ specifying the green color code.
        - This is a required input.
        
        ### `blueValue`
        
        - An _Integer_ specifying the blue color code.
        - This is a required input.
        
        ## Return Code
        
        An _Integer_ specifying color code in Jupiter.
        
        ## Sample Code
        
        ```psj {2}
        # Convert the RGB color code to the color code in Jupiter
        newColor = JPT.ConvertRGBToJPTColor(255,100,213) # Pink color
        JPT.Debugger(newColor)
        ```
        
        """
        message = "JPT.ConvertRGBToJPTColor({},{},{})".format(redValue,greenValue,blueValue)
        return JPT_RUN_LINE(message)

    def ConvertValueToDocUnit(inputValue, unitType):
        r"""
        ## Description
        
        Convert the inputted value from SI\[m\] units (Jupiter macro units) to the current Jupiter unit system.
        
        ## Syntax
        
        ```psj
        JPT.ConvertValueToDocUnit(inputValue, unitType)
        ```
        
        ## Inputs
        
        ### `inputValue`
        
        - A _Double_ which will be used for converting.
        - This is a required input.
        
        ### `unitType`
        
        - An _Enum_ specifying the _[Unit Types](../data-type/psj-utility/pre-utility/enumeration-types/unit-types.md)_ which will be used as the reference for converting.
        - The type of unit can be found at: <menuselection>Home &#187; Preference &#187; Unit</menuselection> in Jupiter.
        - This is a required input.
        
        ## Return Code
        
        A _Double_ specifying the converted value.
        
        ## Sample Code
        
        ```psj {2}
        # Convert 1m in Jupiter macro unit system to the current unit system of Jupiter
        convertToDoc = JPT.ConvertValueToDocUnit(1, JPT.UnitType.Unit_Length)
        JPT.Debugger(convertToDoc)
        ```
        
        """
        message = "JPT.ConvertValueToDocUnit({},{})".format(inputValue,unitType)
        return JPT_RUN_LINE(message)

    def ConvertValueToMacroUnit(inputValue, unitType, outputValueType):
        r"""
        ## Description
        
        Convert the inputted value from the SI\[m\] unit (Jupiter macro unit) to the specified unit.
        The return value will be the value after conversion.
        
        ## Syntax
        
        ```psj
        JPT.ConvertValueToMacroUnit(inputValue, unitType, outputValueType)
        ```
        
        ## Inputs
        
        ### `inputValue`
        
        - A _Double_ which will be used for converting.
        - This is a required input.
        
        ### `unitType`
        
        - An _Enum_ specifying the _[Unit Types](../data-type/psj-utility/pre-utility/enumeration-types/unit-types.md)_ which will be used as the reference for converting.
        - The type of unit can be found at: <menuselection>Home &#187; Preference &#187; Unit</menuselection> in Jupiter.
        - This is a required input.
        
        ### `outputValueType`
        
        - A _String_ specifying the desired unit of the inputted value which will be got after converting from Jupiter macro unit.
        - This is a required input.
        
        ## Return Code
        
        A _Double_ specifying the converted value.
        
        ## Sample Code
        
        ```psj {2}
        # Convert 1m from Jupiter macro unit system to mm
        convertToMacro = JPT.ConvertValueToMacroUnit(1, JPT.UnitType.Unit_Length, 'mm') # 1m -> mm
        JPT.Debugger(convertToMacro) # 1000
        ```
        
        """
        message = "JPT.ConvertValueToMacroUnit({},{},{})".format(inputValue,unitType,outputValueType)
        return JPT_RUN_LINE(message)

    def CreateNewDocument():
        r"""
        ## Description
        
        Create a new document.
        
        ## Syntax
        
        ```psj
        JPT.CreateNewDocument()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[Document](../data-type/psj-utility/pre-utility/built-in-types/Document)_ object that indicate newly created document.
        
        ## Sample Code
        
        ```psj {1}
        JPT.CreateNewDocument()
        ```
        
        """
        message = "JPT.CreateNewDocument({})".format('')
        return JPT_RUN_LINE(message)

    def CreateSubAssembly(subAssemName, parentAssem):
        r"""
        ## Description
        
        Create a new sub assembly under the indicated parent sub assembly.
        
        ## Syntax
        
        ```psj
        JPT.CreateSubAssembly(subAssemName, parentAssem)
        ```
        
        ## Inputs
        
        ### `subAssemName`
        
        - A _String_ specifying the name of the creating sub assembly.
        - This is a required input.
        
        ### `parentAssem`
        
        - A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object specifying the parent sub assembly of the creating sub assembly.
        - If the parent sub assembly is `All Parts` assembly, assigns an instance object _[JPT.DItem()](../data-type/psj-utility/pre-utility/built-in-types/DItem)_.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {2,3,6}
        # Create 2 sub assemblies under All Parts assembly
        JPT.CreateSubAssembly('CreateSubAsm0',JPT.DItem())
        JPT.CreateSubAssembly('CreateSubAsm1',JPT.DItem())
        
        # Create a sub assembly under CreateSubAsm0 (ID = 1)
        JPT.CreateSubAssembly('CreateSubAsm2',JPT.FindSubAssemblyByID(1))
        ```
        
        """
        message = "JPT.CreateSubAssembly({},{})".format(subAssemName,parentAssem)
        return JPT_RUN_LINE(message)

    def CSVExportFormatSetting(int):
        r"""
        ## Description
        
        Set export format of CSV file as with/without BOM.
        
        ## Syntax
        
        ```psj
        JPT.CSVExportFormatSetting(int Selection)
        ```
        
        ## Inputs
        
        ### `int`
        - Selection of export format. 0: without BOM, 1: with BOM.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {1}
        JPT.CSVExportFormatSetting(0)
        ```
        
        """
        message = "JPT.CSVExportFormatSetting({})".format(int)
        return JPT_RUN_LINE(message)

    def Debugger(inputValue):
        r"""
        ## Description
        
        Console debugger for PSJ. This utility will show all the related information of the inputted value to the Python API window.
        
        ## Syntax
        
        ```psj
        JPT.Debugger(inputValue)
        ```
        
        ## Inputs
        
        ### `inputValue`
        
        - A value needing to know its information.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {6}
        # Prepare model
        Geometry.Part.Cube()
        # Get the information of all existing parts
        allParts = JPT.GetAllParts()
        # Print all the related information of the first part to the screen
        JPT.Debugger(allParts[0])
        ```
        
        """
        message = "JPT.Debugger({})".format(inputValue)
        return JPT_RUN_LINE(message)

    def DeleteSubAssembly(subAssembly):
        r"""
        ## Description
        
        Delete the inputted sub assembly.
        
        ## Syntax
        
        ```psj
        JPT.DeleteSubAssembly(subAssembly)
        ```
        
        ## Inputs
        
        ### `subAssembly`
        
        - A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object specifying the sub assembly which will be deleted.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {7}
        # Create 2 sub assemblies under All Parts assemly
        JPT.CreateSubAssembly('CreateSubAsm0',JPT.DItem())
        JPT.CreateSubAssembly('CreateSubAsm1',JPT.DItem())
        
        # Delete the created CreateSubAsm1
        subAssem = JPT.FindSubAssemblyByID(2)
        JPT.DeleteSubAssembly(subAssem)
        ```
        
        """
        message = "JPT.DeleteSubAssembly({})".format(subAssembly)
        return JPT_RUN_LINE(message)

    def DisableMessageBox(messageOptionType):
        r"""
        ## Description
        
        Disable and set default value of the pop-up message box on screen.
        
        ## Syntax
        
        ```psj
        JPT.DisableMessageBox(messageOptionType)
        ```
        
        ## Inputs
        
        ### `messageOptionType`
        
        - An _Enum_ specifying the _[MessageBoxOptionType](../data-type/psj-utility/pre-utility/enumeration-types/msgbox-option-types)_ describing the message option type to be the default value.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {2,7,12,17}
        # Disable pop-up message and set the default value of message box to be YES
        JPT.DisableMessageBox(JPT.MsgBoxOptionType.MB_OPTION_YES)
        returnValue = JPT.MessageBoxPSJ("Test dialog",JPT.MsgBoxType.MB_INFORMATION_YESNO)
        print(returnValue) # Return a string object with value = YES
        
        # Disable pop-up message and set the default value of message box to be NO
        JPT.DisableMessageBox(JPT.MsgBoxOptionType.MB_OPTION_NO)
        returnValue = JPT.MessageBoxPSJ("Test dialog",JPT.MsgBoxType.MB_INFORMATION_YESNO)
        print(returnValue) # Return a string object with value = NO
        
        # Disable pop-up message and set the default value of message box to be CANCEL
        JPT.DisableMessageBox(JPT.MsgBoxOptionType.MB_OPTION_CANCEL)
        returnValue = JPT.MessageBoxPSJ("Test dialog",JPT.MsgBoxType.MB_INFORMATION_YESNOCANCEL)
        print(returnValue) # Return a string object with value = CANCEL
        
        # Disable pop-up message and set the default value of message box to be OK
        JPT.DisableMessageBox(JPT.MsgBoxOptionType.MB_OPTION_OK)
        returnValue = JPT.MessageBoxPSJ("Test dialog",JPT.MsgBoxType.MB_INFORMATION_OKCANCEL)
        print(returnValue) # Return a string object with value = OK
        ```
        
        """
        message = "JPT.DisableMessageBox({})".format(messageOptionType)
        return JPT_RUN_LINE(message)

    def DisableOutputMessage():
        r"""
        ## Description
        
        Disable all the output messages which will be written to the Python API window.
        
        > The output message will be enabled after finishing executing the PSJ code.  
        > Or using _[JPT.EnableOutputMessage()](JPT.EnableOutputMessage)_ to turn it on again.
        
        ## Syntax
        
        ```psj
        JPT.DisableOutputMessage()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {2}
        # Disable the screen animation
        JPT.DisableOutputMessage()
        
        # Print a test message
        # The output message is disabled
        # "Test" string will not be written on the Python API window.
        print("Test")
        ```
        
        """
        message = "JPT.DisableOutputMessage({})".format('')
        return JPT_RUN_LINE(message)

    def DisableOutputMessage_Trunk(messageType):
        r"""
        ## Description
        
        Disable all the output messages which will be written to the Python API window.
        
        > The output message will be enabled after finishing executing the PSJ code.  
        > Or using _[JPT.EnableOutputMessage()](JPT.EnableOutputMessage)_ to turn it on again.
        
        ## Syntax
        
        ```psj
        JPT.DisableOutputMessage(messageType)
        ```
        
        ## Inputs
        
        ### `messageType`
        
        - An _Enum_ specifying the _[MessageConsoleType](../data-type/psj-utility/pre-utility/enumeration-types/msg-console-types)_ describing the message type to be hidden.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {2,8,14}
        # Disable the execution message
        JPT.DisableOutputMessage(JPT.MsgConsoleType.MSG_EXECUTION)
        Geometry.Part.Cube(strName="Cube_2", iPartColor=12934597) # won't print "CreateCube" [0.0, 0.0, 0.0],...
        print("test")
        JPT.Debugger("Test")
        
        # Disable the return message
        JPT.DisableOutputMessage(JPT.MsgConsoleType.MSG_RETURN)
        Geometry.Part.Cube(strName="Cube_2", iPartColor=12934597) # won't print 3:1
        print("test")
        JPT.Debugger("Test")
        
        # Disable the user message (print/debug message)
        JPT.DisableOutputMessage(JPT.MsgConsoleType.MSG_USER)
        Geometry.Part.Cube(strName="Cube_2", iPartColor=12934597)
        print("test") # won't print "test"
        JPT.Debugger("Test") # won't print "Test"
        ```
        
        """
        message = "JPT.DisableOutputMessage_Trunk({})".format(messageType)
        return JPT_RUN_LINE(message)

    def DisableScreenAnimation():
        r"""
        ## Description
        
        Disable screen animation effect.
        
        > The screen animation effect will be enabled after finishing executing the PSJ code.
        > Or using _[JPT.EnableScreenAnimation()](JPT.EnableScreenAnimation)_ to turn it on again.
        
        ## Syntax
        
        ```psj
        JPT.DisableScreenAnimation()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {2}
        # Disable the screen animation
        JPT.DisableScreenAnimation()
        
        # Create a cube and check the screen animation
        # The animation effect is disabled
        Geometry.Part.Cube(iPartColor=7011837)
        ```
        
        """
        message = "JPT.DisableScreenAnimation({})".format('')
        return JPT_RUN_LINE(message)

    def DisableScreenUpdate():
        r"""
        ## Description
        
        Disable updating data render on the display window.
        
        :::note
        
        The data render will be enabled after finishing executing the PSJ code.
        
        :::
        
        ## Syntax
        
        ```psj
        JPT.DisableScreenUpdate()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {2}
        # Disable data render on the display window
        JPT.DisableScreenUpdate()
        
        # Create a cube and check the data render
        # The data render is disabled
        Geometry.Part.Cube(iPartColor=7011837)
        ```
        
        """
        message = "JPT.DisableScreenUpdate({})".format('')
        return JPT_RUN_LINE(message)

    def DItemListToMacroListTCursor(DItemList):
        r"""
        ## Description
        
        Convert _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List_ of _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects to _List of Cursor_ (Macro string type).
        
        ## Syntax
        
        ```psj
        JPT.DItemListToMacroListTCursor(DItemList)
        ```
        
        ## Inputs
        
        ### `DItemList`
        
        - A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or a _List_ of _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects to be converted.
        - This is a required input.
        
        ## Return Code
        
        A _String_ containing all the converted items.
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Get all the existing faces and convert them to List of Cursor (Macro string type)
        ## Get all Faces from model
        listFaces = [JPT.CastToDItem(face) for face in JPT.GetAllFaces()] # List of DItem objects
        ## Return Faces to a string object, for example, return value = [6:73, 6:74, ...]
        JPT.Debugger(JPT.DItemListToMacroListTCursor(listFaces))
        ```
        
        """
        message = "JPT.DItemListToMacroListTCursor({})".format(DItemList)
        return JPT_RUN_LINE(message)

    def DItemToMacroListTCursor(DItem):
        r"""
        ## Description
        
        Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _List of Cursor_ (Macro string type).
        
        ## Syntax
        
        ```psj
        JPT.DItemToMacroListTCursor(DItem)
        ```
        
        ## Inputs
        
        ### `DItem`
        
        - A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to be converted.
        - This is a required input.
        
        ## Return Code
        
        A _String_ containing all the converted items.
        
        ## Sample Code
        
        ```psj {13}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Get all the existing Nodes and convert one of them to List of Cursor (Macro string type)
        ## Get all Nodes from model
        listNodes = [JPT.CastToDItem(node) for node in JPT.GetAllNodes()] # List of DItem objects
        ## Get 1 Node from the created list
        node = listNodes[0] # DItem object
        ## Return Node to a string object, for example, return value = [10:772]
        JPT.Debugger(JPT.DItemToMacroListTCursor(node))
        ```
        
        """
        message = "JPT.DItemToMacroListTCursor({})".format(DItem)
        return JPT_RUN_LINE(message)

    def DItemToMacroTCursor(DItem):
        r"""
        ## Description
        
        Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _Cursor_ (Macro string type).
        
        ## Syntax
        
        ```psj
        JPT.DItemToMacroTCursor(DItem)
        ```
        
        ## Inputs
        
        ### `DItem`
        
        - A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to be converted.
        - This is a required input.
        
        ## Return Code
        
        A _String_ containing all the converted items.
        
        ## Sample Code
        
        ```psj {13}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Get all the existing Nodes and convert one of them to List of Cursor (Macro string type)
        ## Get all Nodes from model
        listNodes = [JPT.CastToDItem(node) for node in JPT.GetAllNodes()] # List of DItem objects
        ## Get 1 Node from the created list
        node = listNodes[0] # DItem object
        ## Return Node to a string object, for example, return value = 10:772
        JPT.Debugger(JPT.DItemToMacroTCursor(node))
        ```
        
        """
        message = "JPT.DItemToMacroTCursor({})".format(DItem)
        return JPT_RUN_LINE(message)

    def DItemToMacroTCursorPair(DItem1, DItem2):
        r"""
        ## Description
        
        Convert pair of _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects to _Cursor_ pair (Macro string type).
        
        ## Syntax
        
        ```psj
        JPT.DItemToMacroTCursorPair(DItem1, DItem2)
        ```
        
        ## Inputs
        
        ### `DItem1`
        
        - The first _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to be converted.
        - This is a required input.
        
        ### `DItem2`
        
        - The second _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to be converted.
        - This is a required input.
        
        ## Return Code
        
        A _String_ containing all the converted items.
        
        ## Sample Code
        
        ```psj {14}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Get all the existing Nodes and convert a pair of them to cursor pair (Macro string type)
        ## Get all Nodes from model
        listNodes = JPT.GetAllNodes() # List of DNode objects
        ## Get 2 Nodes and convert them to DItem object
        dItemNode1 = JPT.CastToDItem(listNodes[0]) # The first DItem object
        dItemNode2 = JPT.CastToDItem(listNodes[1]) # The second DItem object
        ## Return 2 DItems to a string object, for example, return value = 10:772-10:251
        JPT.Debugger(JPT.DItemToMacroTCursorPair(dItemNode1, dItemNode2))
        ```
        
        """
        message = "JPT.DItemToMacroTCursorPair({},{})".format(DItem1,DItem2)
        return JPT_RUN_LINE(message)

    def DrawArrow(listStartPoint , listEndPoint , color, width, bothSides, threeDArrow=True):
        r"""
        ## Description
        
        Draw an arrow in Main Window.
        
        ## Syntax
        
        ```psj
        JPT.DrawArrow()
        ```
        
        ## Inputs
        
        ### `listStartPoint `
        
        - A list specifying the coordinates of the starting point of the arrow (e.g., [x1, y1, z1]). 
          - The value is in SI units [meters].
          
        ### `listEndPoint `
        - A list specifying the coordinates of the ending point of the arrow (e.g., [x2, y2, z2]). 
          - The value is in SI units [meters].
          
        ### `color`
        - An _Int_ in hexadecimal format representing the arrow's color. 
        - The default color is cyan (RGB(0, 255, 255)).
        
        ### `width`
        - A _Float_ specifying the the width of the arrow's shaft in pixels. The default is 1.0.
        
        ### `bothSides`
        - A _Bool_ specifying the drawing arrow direction.
          - _False_: the program will draw only one specified arrow.
          - _True_: the program will draw two arrows -  one pointing from the starting point to the endpoint and another pointing in the reverse direction. 
        - The default valueis _False_.
        
        ###  `threeDArrow`
        - A _Bool_ specifying arrow style. 
          - _True_: the arrow will be drawn in 3D style. 
          - _False_: it will be drawn as a flat arrow. 
        - The default value is _True_.
        
        ## Return Code
        
        - A _Boolean_ specifying Succeeded or Failed.
          - True: Succeeded.
          - False: Failed.
        
        ## Sample Code
        
        ```psj {6,9,12,14}
        #Prepare a model for view
        Geometry.Part.Cube(dlLength=[10.0, 10.0, 10.0])
        JPT.ViewFitToModel()
        
        #Draw a cyan arrow from [0, 0, 0] to [10, 20, 30] with default width and style:
        JPT.DrawArrow([0, 0, 0], [10, 20, 30])
        
        #Draw a red arrow from [5, 5, 5] to [15, 15, 15] with width 2.5 pixels:
        JPT.DrawArrow([5, 5, 5], [15, 15, 15], 255, 2.5)
        
        #Draw a green arrow with arrows pointing in both directions:
        JPT.DrawArrow([1, 1, 1], [4, 4, 4], 65280, 1.5, True)
        
        #Draw a blue arrow in 2D style from [2, 2, 0] to [4, 4, 0] with default width:
        JPT.DrawArrow([2, 2, 0], [4, 4, 0], 16711680, 1.0, False, False)
        ```
        
        """
        message = "JPT.DrawArrow({},{},{},{},{},{})".format(listStartPoint ,listEndPoint ,color,width,bothSides,threeDArrow)
        return JPT_RUN_LINE(message)

    def DrawLine(listStartPoint, listEndPoint, color, width):
        r"""
        ## Description
        
        Draw a line in Main Window
        
        ## Syntax
        
        ```psj
        JPT.DrawLine()
        ```
        
        ## Inputs
        
        ### `listStartPoint`
        
        - A _list_ specifying the coordinates of the the starting point of the line (e.g., [x1, y1, z1]). 
        - The value is in SI units [meters].
        
        ### `listEndPoint`
        - A _list_ specifying the coordinates of the the ending point of the line (e.g., [x2, y2, z2]). 
        - The value is in SI units [meters].
        
        ### `color`
        - An _Int_ in hexadecimal format representing the arrow's color. 
        - The default color is cyan (RGB(0, 255, 255)).
        
        ### `width`
        - An _Int_ specifying the width of the arrow's shaft in pixels. 
        - The default is 1.
        
        ## Return Code
        
        - A _Boolean_ specifying Succeeded or Failed.
          - True: Succeeded.
          - False: Failed.
        
        ## Sample Code
        
        ```psj {6,9,12}
        #Prepare a model for view
        Geometry.Part.Cube(dlLength=[10.0, 10.0, 10.0])
        JPT.ViewFitToModel()
        
        # Draw a white line from [0, 0, 0] to [10, 20, 30] with the default color and width:
        JPT.DrawLine([0, 0, 0], [10, 20, 30])
        
        # Draw a red line from [5, 5, 5] to [15, 15, 15] with a width of 2.5:
        JPT.DrawLine([5, 5, 5], [15, 15, 15], 255, 2.5)
                
        # Draw a green line from [1, 1, 1] to [2, 2, 2] with a width of 1.5:
        JPT.DrawLine([1, 1, 1], [2, 2, 2], 65280, 1.5)
        ```
        
        """
        message = "JPT.DrawLine({},{},{},{})".format(listStartPoint,listEndPoint,color,width)
        return JPT_RUN_LINE(message)

    def DrawPoint(listPosition  , color, width):
        r"""
        ## Description
        
        Draw a point in Main Window.
        
        ## Syntax
        
        ```psj
        JPT.DrawPoint()
        ```
        
        ## Inputs
        
        ### `listPosition  `
        
        - A list specifying the coordinates of the the position of the point (e.g., [x, y, z]). 
          - The value is in SI units [meters].
          
        ### `color`
        - An _Int_ in hexadecimal format representing the arrow's color. 
        - The default color is cyan (RGB(0, 255, 255)).
        
        ### `width`
        - A _Float_ (float): The width of the arrow's shaft in pixels. The default is 1.0.
        
        ## Return Code
        
        - A _Boolean_ specifying Succeeded or Failed.
          - True: Succeeded.
          - False: Failed.
        
        ## Sample Code
        
        ```psj {6,9,12}
        #Prepare a model for view
        Geometry.Part.Cube(dlLength=[10.0, 10.0, 10.0])
        JPT.ViewFitToModel()
        
        # Draw a green point at position [10, 20, 30] with the default color and width:
        JPT.DrawPoint([10, 20, 30])
        
        # Draw a red point at position [5, 15, 25] with a width of 2.5:
        JPT.DrawPoint([5, 15, 25], 255, 2.5)
        
        # Draw a blue point at position [0, 0, 0] with a width of 1.5:
        JPT.DrawPoint([0, 0, 0], 16711680, 1.5)
        ```
        
        """
        message = "JPT.DrawPoint({},{},{})".format(listPosition  ,color,width)
        return JPT_RUN_LINE(message)

    def DrawRect(left , top, right, bottom, color, width):
        r"""
        ## Description
        
        Draw a rectangle on Main Window by window coordinate.
        
        ## Syntax
        
        ```psj
        JPT.DrawRect()
        ```
        
        ## Inputs
        
        ### `left `
        - An _Int_ specifying the x-coordinate of the left edge of the rectangle, in pixels.
        
        ### `top`
        - An _Int_ specifying the Y-coordinate of the top edge of the rectangle, in pixels.
        
        ### `right`
        - An _Int_ specifying the x-coordinate of the right edge of the rectangle, in pixels.
        
        ### `bottom`
        - An _Int_ specifying the y-coordinate of the bottom edge of the rectangle, in pixels.
        
        ### `color`
        - An _Int_ in hexadecimal format representing the arrow's color. 
        - The default color is cyan (RGB(0, 255, 255)).
        
        ### `width`
        - An _Int_ specifying the width of the arrow's shaft in pixels. 
        - The default is 1.
        
        ## Return Code
        
        - A _Boolean_ specifying Succeeded or Failed.
          - True: Succeeded.
          - False: Failed.
        
        ## Sample Code
        
        ```psj {6,12,18}
        JPT.ClearDraw()
        # Draw a rectangle with 
        # top-left corner at (10, 20) 
        # bottom-right corner at (50, 100)
        # in pixels
        JPT.DrawRect(10, 20, 50, 100)
        
        # Draw a rectangle in red with  
        # top-left corner at (100, 200) 
        # and bottom-right corner at (400, 400)
        # in pixels
        JPT.DrawRect(100, 200, 400, 400, 255)
        
        # Draw a rectangle in yellow, width=5 with 
        # top-left corner at (100, 10) 
        # bottom-right corner at (200, 100)
        # in pixels
        JPT.DrawRect(100, 10, 200, 100, JPT.ConvertRGBToJPTColor(255,255,0), 5)
        
        ```
        
        """
        message = "JPT.DrawRect({},{},{},{},{},{})".format(left ,top,right,bottom,color,width)
        return JPT_RUN_LINE(message)

    def DTVector3dToMacroVector(DTVector3d):
        r"""
        ## Description
        
        Convert _[TVector3d](../data-type/psj-utility/pre-utility/built-in-types/TVector3d)_ object to DTVector3d (Macro string type).
        
        ## Syntax
        
        ```psj
        JPT.DTVector3dToMacroVector(DTVector3d)
        ```
        
        ## Inputs
        
        ### `DTVector3d`
        
        - A _[TVector3d](../data-type/psj-utility/pre-utility/built-in-types/TVector3d)_ object to be converted.
        - This is a required input.
        
        ## Return Code
        
        A _String_ containing all the converted items.
        
        ## Sample Code
        
        ```psj {13}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Get all the existing Nodes and convert one of them to DTVector3D (Macro string type)
        ## Get all Nodes from model
        listNodes = JPT.GetAllNodes() # List of DNode objects
        ## Get position (DTVector3D) of 1 node in list
        posNode1 = listNodes[0].pos # DTVector3D object
        # Return DTVector3D object to a string object, for example, return value = [0,0.00777778,0.00444444]
        JPT.Debugger(JPT.DTVector3dToMacroVector(posNode1))
        ```
        
        """
        message = "JPT.DTVector3dToMacroVector({})".format(DTVector3d)
        return JPT_RUN_LINE(message)

    def EnableAllLicenses(BoolType):
        r"""
        ## Description
        
        Enable/Disable all the licenses feature which is existing in the current Jupiter.
        
        ## Syntax
        
        ```psj
        JPT.EnableAllLicenses(...)
        ```
        
        ## Inputs
        
        ### `BoolType`
        
        - A _Bool_ describing the enable state of license:
          - _True_: Enable all the licenses.
          - _False_: Disable all the licenses.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {2}
        # Disable all the licenses
        JPT.EnableAllLicenses(False)
        ```
        
        """
        message = "JPT.EnableAllLicenses({})".format(BoolType)
        return JPT_RUN_LINE(message)

    def EnableLicenseFeature(licenseFeatureName, BoolType):
        r"""
        ## Description
        
        Enable/Disable a license feature which is existing in the current Jupiter.
        
        ## Syntax
        
        ```psj
        JPT.EnableLicenseFeature("licenseFeatureName", BoolType)
        ```
        
        ## Inputs
        
        ### `licenseFeatureName`
        
        - A _String_ specifying the name of Jupiter license which is existing in the current Jupiter.
        - The Jupiter license's name can be found at <menuselection>Home &#187; Preference &#187; License</menuselection>.
        - This is a required input.
        
        ### `BoolType`
        
        - An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the enable state of license:
          - _True_: Enable the license.
          - _False_: Disable the license.
        - This is a required input.
        
        :::tip
        You also can input **1** instead of inputting JPT.BoolType.TRUE_VAL,
        or input **0** instead of inputting JPT.BoolType.FALSE_VAL.
        :::
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {2,3,5,8,9,11}
        # Disable license JPT_BASE
        JPT.EnableLicenseFeature("JPT_BASE",
                                 JPT.BoolType.FALSE_VAL)
        # Or
        # JPT.EnableLicenseFeature("JPT_BASE", 0)
        
        # Enable license JPT_BASE
        JPT.EnableLicenseFeature("JPT_BASE",
                                 JPT.BoolType.TRUE_VAL)
        # Or
        # JPT.EnableLicenseFeature("JPT_BASE", 1)
        ```
        
        """
        message = "JPT.EnableLicenseFeature({},{})".format(licenseFeatureName,BoolType)
        return JPT_RUN_LINE(message)

    def EnableOutputMessage():
        r"""
        ## Description
        
        Enable the output message which will be written to the Python API window.
        
        > This utility is used to enable the output message on the Python API window after using the _[JPT.DisableOutputMessage()](JPT.DisableOutputMessage)_ utility.
        
        ## Syntax
        
        ```psj
        JPT.EnableOutputMessage()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {11}
        # Disable the screen animation
        JPT.DisableOutputMessage()
        
        # Print a string to test the output message
        # on the Python API window
        # The string will not be printed on the Python API window
        print("Test")
        
        # Enable the output message on the Python API window
        # after using JPT.DisableOutputMessage()
        JPT.EnableOutputMessage()
        
        # Print a string to test the output message
        # on the Python API window
        # The string will be printed on the Python API window
        print("Test")
        ```
        
        """
        message = "JPT.EnableOutputMessage({})".format('')
        return JPT_RUN_LINE(message)

    def EnableScreenAnimation():
        r"""
        ## Description
        
        Enable screen animation effect.
        
        > This utility is used to enable the screen animation effect after using the _[JPT.DisableScreenAnimation()](JPT.DisableScreenAnimation)_ utility.
        
        ## Syntax
        
        ```psj
        JPT.EnableScreenAnimation()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {9}
        # Disable the screen animation
        JPT.DisableScreenAnimation()
        
        # Create a cube and check the screen animation
        # The animation effect is disabled
        Geometry.Part.Cube(iPartColor=7011837)
        
        # Enable the screen animation effect after using JPT.DisableScreenAnimation()
        JPT.EnableScreenAnimation()
        
        # Create a cube and check the screen animation
        # The animation effect will be enabled
        Geometry.Part.Cube(iPartColor=7011837)
        ```
        
        """
        message = "JPT.EnableScreenAnimation({})".format('')
        return JPT_RUN_LINE(message)

    def EnableScreenUpdate():
        r"""
        ## Description
        
        Enable data render on the screen.
        
        > This utility is used to enable the data render after using the _[JPT.DisableScreenUpdate()](JPT.DisableScreenUpdate)_ utility.
        
        ## Syntax
        
        ```psj
        JPT.EnableScreenUpdate()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {9}
        # Disable data render on the display window
        JPT.DisableScreenUpdate()
        
        # Create a cube and check the data render
        # The data render is disabled
        Geometry.Part.Cube(iPartColor=7011837)
        
        # Enable the data render after using JPT.DisableScreenUpdate()
        JPT.EnableScreenUpdate()
        
        # Create a cube and check data render
        # The data render will be enabled
        Geometry.Part.Cube(iPartColor=7011837)
        ```
        
        """
        message = "JPT.EnableScreenUpdate({})".format('')
        return JPT_RUN_LINE(message)

    def EndDatabaseTransaction():
        r"""
        ## Description
        
        Enable data transaction again, after using [JPT.BeginDatabaseTransaction()](JPT.BeginDatabaseTransaction).
        
        ## Syntax
        
        ```psj
        JPT.EndDatabaseTransaction()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {83}
        # Begin Data Base Transaction
        JPT.BeginDatabaseTransaction("Make meshed model")
        
        # From now on, all the steps inside will be stored as one step - "Make meshed model".
        # You can check it by clicking on the Undo button after the execution process is finished.
        
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                           strName="Cube_2",
                           iPartColor=6409934)
        Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0],
                           strName="Cube_3",
                           iPartColor=13259210)
        Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0],
                           strName="Cube_4",
                           iPartColor=7697908)
        Geometry.Part.Cube(dlOrigin=[0.04, 0.0, 0.0],
                           strName="Cube_5",
                           iPartColor=7463537)
        Geometry.Part.Cube(dlOrigin=[0.05, 0.0, 0.0],
                           strName="Cube_6",
                           iPartColor=7434735)
        Geometry.Part.Cube(dlOrigin=[0.06, 0.0, 0.0],
                           strName="Cube_7",
                           iPartColor=14903267)
        Geometry.Part.Cube(dlOrigin=[0.07, 0.0, 0.0],
                           strName="Cube_8",
                           iPartColor=15658599)
        
        Meshing.SetMeshAttribute(crlParts=[Part(5, 6, 7, 8)],
                                 surfaceMesh=SURFACE_MESH(dGeomAngle=0.7853981634,
                                                          iPerformanceMode=1,
                                                          dAutoMergeTinyFacesAngle=0.5235987756,
                                                          bOutputQuadMesh=True,
                                                          bGeomApprox=True,
                                                          iNextEntityOffsetId=0))
        Meshing.SurfaceMeshing(crlParts=[Part(5, 6, 7, 8)],
                               surfaceMesh=SURFACE_MESH(dGeomAngle=0.7853981634,
                                                        iPerformanceMode=1,
                                                        dAutoMergeTinyFacesAngle=0.5235987756,
                                                        bOutputQuadMesh=True,
                                                        bGeomApprox=True,
                                                        iNextEntityOffsetId=0),
                                                        iThreadNum=12)
        MeshEdit.SurfaceMesh(crlParts=[Part(2, 4, 8, 6)])
        Meshing.SolidMeshing(crlParts=[Part(8, 4, 7, 3)],
                             dGradingFactor=1.05,
                             dStretchLimit=0.1,
                             iSpeedVsQual=1,
                             iRegion=1,
                             bSafeMode=False,
                             iParallel=12,
                             bInternalMeshOnly=False,
                             iPartColor=65280)
        Meshing.SolidMeshing(crlParts=[Part(4)],
                             bTet10=True,
                             dGradingFactor=1.05,
                             dStretchLimit=0.1,
                             iSpeedVsQual=1,
                             iRegion=1,
                             bSafeMode=False,
                             iParallel=12,
                             bInternalMeshOnly=False,
                             iPartColor=65280)
        
        del_faces = [208, 182, 178, 204, 206, 177, 203, 179, 205, 180]
        extrude_faces = [207, 181]
        
        Geometry.DeleteEntity.Face(crlFaces=[Face(*del_faces)])
        
        HexModeling.Linear(crlFaces=[Face(*extrude_faces)],
                           dLength=0.01,
                           iLayer=2,
                           vecSweepDirection=[0.0,
                                              0.0,
                                              1.0],
                           iLinearMethod=4)
        
        MeshEdit.SolidMesh(crlParts=[Part(8)])
        
        # End Data Base Transaction
        JPT.EndDatabaseTransaction()
        ```
        
        """
        message = "JPT.EndDatabaseTransaction({})".format('')
        return JPT_RUN_LINE(message)

    def Exec(macroCommand):
        r"""
        ## Description
        
        Run Jupiter macro.
        
        ## Syntax
        
        ```psj
        JPT.Exec(macroCommand)
        ```
        
        ## Inputs
        
        ### `macroCommand`
        
        - A _String_ specifying the macro command.
        - This is a required input.
        
        ## Return Code
        
        Based on the output of the inputted macro command.
        
        ## Sample Code
        
        ```psj {2,3}
        # Create a cube and store its cursor
        createdCube = JPT.Exec('CreateCube([0, 0, 0], [0.01, 0.01, 0.01], \
                                [10, 10, 10], "Cube_1", 12999622, 0:0)')
        JPT.Debugger(createdCube) # Return a string object with value = 3:1
        ```
        
        """
        message = "JPT.Exec({})".format(macroCommand)
        return JPT_RUN_LINE(message)

    def ExpandAssemblyTree():
        r"""
        ## Description
        
        Expand all the items existing on the Assembly window.
        
        > This utility is used to expand all the items existing on the Assembly window after using _[JPT.CollapseAssemblyTree()](JPT.CollapseAssemblyTree)_ utility.
        
        ## Syntax
        
        ```psj
        JPT.ExpandAssemblyTree()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {33}
        # Preparing tree
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2", iPartColor=6409934)
        Geometry.Part.Cube(strName="Cube_3", iPartColor=13259210)
        Geometry.Part.Cube(strName="Cube_4", iPartColor=7697908)
        Geometry.Part.Cube(strName="Cube_5", iPartColor=7463537)
        Geometry.Part.Cube(strName="Cube_6", iPartColor=7434735)
        Geometry.Part.Cube(strName="Cube_7", iPartColor=14903267)
        Geometry.Part.Cube(strName="Cube_8", iPartColor=15658599)
        Geometry.Part.Cube(strName="Cube_9", iPartColor=7961077)
        Geometry.Part.Cube(strName="Cube_10", iPartColor=7829501)
        Geometry.Part.Cube(strName="Cube_11", iPartColor=11842649)
        Geometry.Part.Cube(strName="Cube_12", iPartColor=14968422)
        Geometry.Part.Cube(strName="Cube_13", iPartColor=6250447)
        Geometry.Part.Cube(strName="Cube_14", iPartColor=12734402)
        Assembly.RightClick.AddSubAssembly()
        Assembly.RightClick.AddSubAssembly()
        Assembly.RightClick.AddSubAssembly(crInst=Inst(1))
        Assembly.RightClick.AddSubAssembly(crInst=Inst(2))
        Assembly.RightClick.AddSubAssembly(crInst=Inst(4))
        Assembly.RightClick.AddSubAssembly(crInst=Inst(5))
        Assembly.RightClick.AddSubAssembly(crInst=Inst(3))
        Assembly.RightClick.AddSubAssembly(crInst=Inst(6))
        Assembly.RightClick.AddSubAssembly(crInst=Inst(7))
        Assembly.RightClick.AddSubAssembly(crInst=Inst(7))
        Assembly.RightClick.AddSubAssembly(crInst=Inst(7))
        Connections.MPC.General.NodesToNodes(crlMasterNodes=[Node(6425)], crlSlaveNodes=[Node(6776)], listMpcConnection=[MPC_CONNECTION(iDof=1), MPC_CONNECTION(iDof=2), MPC_CONNECTION(iDof=4), MPC_CONNECTION(), MPC_CONNECTION(), MPC_CONNECTION()], bUpdateDispCS=1)
        Connections.MPC.General.NodesToNodes(strName="MPC_2", crlMasterNodes=[Node(6776)], crlSlaveNodes=[Node(6775)], listMpcConnection=[MPC_CONNECTION(iDof=1), MPC_CONNECTION(iDof=2), MPC_CONNECTION(iDof=4), MPC_CONNECTION(), MPC_CONNECTION(), MPC_CONNECTION()], bUpdateDispCS=1)
        Connections.MPC.General.NodesToNodes(strName="MPC_3", crlMasterNodes=[Node(6775)], crlSlaveNodes=[Node(6774)], listMpcConnection=[MPC_CONNECTION(iDof=1), MPC_CONNECTION(iDof=2), MPC_CONNECTION(iDof=4), MPC_CONNECTION(), MPC_CONNECTION(), MPC_CONNECTION()], bUpdateDispCS=1)
        Connections.MPC.General.NodesToNodes(strName="MPC_4", crlMasterNodes=[Node(6774)], crlSlaveNodes=[Node(6773)], listMpcConnection=[MPC_CONNECTION(iDof=1), MPC_CONNECTION(iDof=2), MPC_CONNECTION(iDof=4), MPC_CONNECTION(), MPC_CONNECTION(), MPC_CONNECTION()], bUpdateDispCS=1)
        
        # Expand all the items existing on the Assembly window
        JPT.ExpandAssemblyTree()
        
        # Collapse all the collapsed items existing on the Assembly window
        JPT.CollapseAssemblyTree()
        ```
        
        """
        message = "JPT.ExpandAssemblyTree({})".format('')
        return JPT_RUN_LINE(message)

    def FindSubAssemblyByID(subAssemID):
        r"""
        ## Description
        
        Get the related information of the target sub assembly by its ID.
        
        ## Syntax
        
        ```psj
        JPT.FindSubAssemblyByID(subAssemID)
        ```
        
        ## Inputs
        
        ### `subAssemID`
        
        - An _Integer_ specifying the ID of the target sub assembly.
        - This is a required input.
        
        ## Return Code
        
        A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object specifying the information of the target sub assembly.
        
        ## Sample Code
        
        ```psj {7}
        # Create 2 sub assemblies under All Parts assembly
        JPT.CreateSubAssembly('CreateSubAsm0',JPT.DItem())
        JPT.CreateSubAssembly('CreateSubAsm1',JPT.DItem())
        JPT.ViewFitToModel()
        
        # Get the information of the sub assembly with ID = 1
        JPT.Debugger(JPT.FindSubAssemblyByID(1))
        ```
        
        """
        message = "JPT.FindSubAssemblyByID({})".format(subAssemID)
        return JPT_RUN_LINE(message)

    def FindSubAssemblyByName(subAssemName):
        r"""
        ## Description
        
        Get the related information of the target sub assembly by its name.
        
        ## Syntax
        
        ```psj
        JPT.FindSubAssemblyByName(subAssemName)
        ```
        
        ## Inputs
        
        ### `subAssemName`
        
        - A _String_ specifying the name of the target sub assembly.
        - This is a required input.
        
        ## Return Code
        
        A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or a _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ specifying found sub assemblies.
        
        ## Sample Code
        
        ```psj {7}
        # Create 2 sub assemblies under All Parts assembly
        JPT.CreateSubAssembly('CreateSubAsm0',JPT.DItem())
        JPT.CreateSubAssembly('CreateSubAsm1',JPT.DItem())
        JPT.ViewFitToModel()
        
        # Get the information of the sub assembly with name = CreateSubAsm0
        JPT.Debugger(JPT.FindSubAssemblyByName('CreateSubAsm0'))
        
        ```
        
        """
        message = "JPT.FindSubAssemblyByName({})".format(subAssemName)
        return JPT_RUN_LINE(message)

    def GetActiveDataOption():
        r"""
        ## Description
        
        Get the active Post Data Option of the working result.
        
        ## Syntax
        
        ```psj
        JPT.GetActiveDataOption()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[PostDataOp](../data-type/psj-utility/post-utility/post-built-in-types/post-data-op)_ object containing the active setting of the working result.
        
        ## Sample Code
        
        ```psj {19}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
        
        default_result_option = \
            JPT.GetDefaultResultOption(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,
                                       1,
                                       1,
                                       "Stress",
                                       "XX",
                                       JPT.PostResultDataLoc.POST_LOC_ON_ELEMENT_NODE)
        
        JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XX, 2}, {1, 1, 0, 0, 16, 0, \
                                     0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                                     0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, \
                                     0, 0, 0, 0.000000, 0}, 0, 0)')
        
        active_result_option = JPT.GetActiveDataOption()
        JPT.Debugger(default_result_option)
        JPT.Debugger(active_result_option)
        ```
        
        """
        message = "JPT.GetActiveDataOption({})".format('')
        return JPT_RUN_LINE(message)

    def GetActiveDocument():
        r"""
        ## Description
        
        Get information of active document.
        
        ## Syntax
        
        ```psj
        JPT.GetActiveDocument()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[Document](../data-type/psj-utility/pre-utility/built-in-types/Document)_ object specifying the information of document.
        
        ## Sample Code
        
        ```psj {5}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
        # Get information of active document
        doc = JPT.GetActiveDocument()
        JPT.Debugger(doc)
        ```
        
        """
        message = "JPT.GetActiveDocument({})".format('')
        return JPT_RUN_LINE(message)

    def GetActivePostJob():
        r"""
        ## Description
        
        Get information of active Post Job.
        
        ## Syntax
        
        ```psj
        JPT.GetActivePostJob()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object specifying the information of the active Post Job.
        
        ## Sample Code
        
        ```psj {5}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        post_job = JPT.GetActivePostJob()
        JPT.Debugger(post_job)
        ```
        
        """
        message = "JPT.GetActivePostJob({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllAvailableResultOptions(PostAnalysisType, resultSet, timeStep, resultName, componentName, PostResultDataLoc):
        r"""
        ## Description
        
        Get all available result options of the inputted result type.
        
        ## Syntax
        
        ```psj
        JPT.GetAllAvailableResultOptions(PostAnalysisType,
                                         resultSet,
                                         timeStep,
                                         resultName,
                                         componentName,
                                         PostResultDataLoc)
        ```
        
        ## Inputs
        
        ### `PostAnalysisType`
        
        - An _Enum_ specifying the _[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.
        - This is a required input.
        
        ### `resultSet`
        
        - An _Integer_ specifying the step ID of the imported result.
        - This is a required input.
        
        ### `timeStep`
        
        - An _Integer_ specifying the time step of the imported result.
        - This is a required input.
        
        ### `resultName`
        
        - A _String_ specifying the type of result (Such as Displacement, Stress, etc.).
        - This is a required input.
        
        ### `componentName`
        
        - A _String_ specifying a specific direction of the result (Such as X, Y, Z, etc.).
        - This is a required input.
        
        ### `PostResultDataLoc`
        
        - An _Enum_ specifying the _[PostResultDataLoc](../data-type/psj-utility/post-utility/enumeration-types/post-result-data-loc-types)_ describing the location of result (Such as on node, on element, etc.).
        - This is a required input.
        
        ## Return Code
        
        A _List of [PostDataOp](../data-type/psj-utility/post-utility/post-built-in-types/post-data-op)_ objects specifying all available settings of the working result.
        
        ## Sample Code
        
        ```psj {5-13}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        all_available_result_options_vector = \
            JPT.GetAllAvailableResultOptions(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,
                                             1,
                                             1,
                                             "Stress",
                                             "XX",
                                             JPT.PostResultDataLoc.POST_LOC_ON_ELEMENT_NODE
                                            )
        
        JPT.Debugger(all_available_result_options_vector)
        
        for available_PostDataOp in all_available_result_options_vector:
            #Component of AvailablePostDataOp
            print("---------------------------------")
            print("Location: " + str(available_PostDataOp.loc))
            print("Conversion: " + str(available_PostDataOp.cnv))
            print("Continuously: " + str(available_PostDataOp.cont))
            print("Coordinate: " + str(available_PostDataOp.coord))
            print("Load 1D: " + str(available_PostDataOp.load1d))
            print("Load 2D: " + str(available_PostDataOp.load2d))
            print("Complex: " + str(available_PostDataOp.complex))
            print("Phase Angle: " + str(available_PostDataOp.phaseAngle))
            print("User Coordinate ID: " + str(available_PostDataOp.userCoordSysId))
        ```
        
        <!-- [//]: # "amt is not used in the current version"
        
        <!-- print("Amplitude: " + str(available_PostDataOp.amt)) -->
        
        """
        message = "JPT.GetAllAvailableResultOptions({},{},{},{},{},{})".format(PostAnalysisType,resultSet,timeStep,resultName,componentName,PostResultDataLoc)
        return JPT_RUN_LINE(message)

    def GetAllByTableTypeID(DTableType):
        r"""
        ## Description
        
        Get all the information of all entities by inputting _[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_.
        
        ## Syntax
        
        ```psj
        JPT.GetAllByTableTypeID(DTableType)
        ```
        
        ## Inputs
        
        ### `DTableType`
        
        - An _Enum_ specifying _[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_ of the target entities.
        - This is a required input.
        
        ## Return Code
        
        A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing all the information of all the found entities by inputted ID.
        
        ## Sample Code
        
        ```psj {8}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Select all parts and store their information to a list of DItem
        listDTableParts = JPT.GetAllByTableTypeID(JPT.DTableType.DTABLE_BODY) # ID = 5
        JPT.Debugger(listDTableParts)
        
        ```
        
        """
        message = "JPT.GetAllByTableTypeID({})".format(DTableType)
        return JPT_RUN_LINE(message)

    def GetAllByTypeID(DItemType):
        r"""
        ## Description
        
        Get all the information of all entities by inputting _[DItemType](../data-type/psj-command/DItem-types)_.
        
        ## Syntax
        
        ```psj
        JPT.GetAllByTypeID(DItemType)
        ```
        
        ## Inputs
        
        ### `DItemType`
        
        - An _Enum_ specifying _[DItemType](../data-type/psj-command/DItem-types)_ of the target entities.
        - This is a required input.
        
        ## Return Code
        
        A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing all the information of all the found entities by inputted ID.
        
        ## Sample Code
        
        ```psj {8}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Select all parts and store their information to a list of DItem
        listDItemParts = JPT.GetAllByTypeID(JPT.DItemType.BODY) # ID = 3
        JPT.Debugger(listDItemParts)
        ```
        
        """
        message = "JPT.GetAllByTypeID({})".format(DItemType)
        return JPT_RUN_LINE(message)

    def GetAllConnections():
        r"""
        ## Description
        
        Get all the information of all existing connections.
        
        ## Syntax
        
        ```psj
        JPT.GetAllConnections()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[ConnectVector](../data-type/psj-utility/pre-utility/built-in-types/ConnectVector)_ object or _List of [DConnect](../data-type/psj-utility/pre-utility/built-in-types/DConnect)_ objects containing all the information of all the existing connections.
        
        ## Sample Code
        
        ```psj {19}
        # Prepare model
        Geometry.Part.Cube(iPartColor=13290083)
        Geometry.Part.Cube(dlOrigin=[0.012, 0.0, 0.0], strName="Cube_2", iPartColor=6149981)
        Geometry.Part.Cube(dlOrigin=[0.024, 0.0, 0.0], strName="Cube_3", iPartColor=7664244)
        Geometry.Part.Cube(dlOrigin=[0.036, 0.0, 0.0], strName="Cube_4", iPartColor=13588687)
        Geometry.Part.Cube(dlOrigin=[0.036, 0.012, 0.0], strName="Cube_5", iPartColor=14048091)
        Geometry.Part.Cube(dlOrigin=[0.024, 0.012, 0.0], strName="Cube_6", iPartColor=7138156)
        Geometry.Part.Cube(dlOrigin=[0.012, 0.012, 0.0], strName="Cube_7", iPartColor=5489235)
        Geometry.Part.Cube(dlOrigin=[0.0, 0.012, 0.0], strName="Cube_8", iPartColor=7632109)
        Connections.MPC.General.NodesToNodes(crlMasterNodes=[Node(1932)], crlSlaveNodes=[Node(1429)], listMpcConnection=[MPC_CONNECTION(iDof=1), MPC_CONNECTION(iDof=2), MPC_CONNECTION(iDof=4), MPC_CONNECTION(), MPC_CONNECTION(), MPC_CONNECTION()], bUpdateDispCS=1)
        Connections.RigidElements.RBE2.OneToOne(crlMasterTargets=[Node(940)], crlSlaveTargets=[Node(3363)])
        Connections.RigidElements.RBE3.OneToMany(crlMasterTargets=[Node(459, 3889, 3859)], crlSlaveTargets=[Node(3879)], listRbe3TermConnection=[(0, 63, 1), (1, 7, 3)], strName="RBE3_1")
        Connections.SpringsDampers.Spring.OneToOne.sameDoFs(iMethod=17, strName="Spring_2", crlMasterTargets=[Node(2396)], crlSlaveTargets=[Node(2428)], iSpringType=2, posTStiffness=[1.7976931e+308, 1.7976931e+308, 1.7976931e+308], posRStiffness=[1.7976931e+308, 1.7976931e+308, 1.7976931e+308])
        Connections.SpringsDampers.Bush.TwoNodes(crlMaster=[Node(2884)], crlSlave=[Node(2900)], iOriMode=1, dlVector=[0, 0, 0], dlStiffness=[DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL], dlDampCoef=[DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL], dlDampConst=[DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL, DFLT_DBL])
        Connections.SpringsDampers.Damper.AnyEntities11DoFS(iMethod=17, strName="Damper_1", crlMasterTargets=[Node(3382)], crlSlaveTargets=[Node(3398)])
        JPT.ViewFitToModel()
        
        # Get all the existing connections
        listDConnections = JPT.GetAllConnections()
        JPT.Debugger(listDConnections)
        
        # Print all the relating information of each existing connection in list
        for connection in listDConnections:
            JPT.Debugger(connection)
        ```
        
        """
        message = "JPT.GetAllConnections({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllContacts():
        r"""
        ## Description
        
        Get all the information of all existing contacts.
        
        ## Syntax
        
        ```psj
        JPT.GetAllContacts()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[ContactVector](../data-type/psj-utility/pre-utility/built-in-types/DContactVector)_ object or _List of [DContact](../data-type/psj-utility/pre-utility/built-in-types/DContact)_ objects containing all the information of all the existing custom notes.
        
        ## Sample Code
        
        ```psj {35}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
        Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
        JPT.ViewFitToModel()
        
        Tools.Group.CreateGroup(strGroupName="Cube_2(49)-G0002", crlTargets=[Face(49)])
        Tools.Group.CreateGroup(strGroupName="Cube_1(24)-G0001", crlTargets=[Face(24)])
        
        Connections.Contacts.TSSS.ContactTable(
            strName="C0001_Cube_2-G0002_Cube_1-G0001", 
            sunshineContact=SUNSHINE_CONTACT(
                iType=1, 
                dERROR=0.001, 
                dFRIC=DFLT_DBL, 
                dSLIDE=DFLT_DBL, 
                iICOORD=1, 
                dSFACT=DFLT_DBL, 
                dSFACTT=DFLT_DBL), 
            crplTarget=[CursorPair(Group(1), Group(2))], iColor=65280)
        Tools.Group.CreateGroup(strGroupName="Cube_3(75)-G0004", crlTargets=[Face(75)])
        Tools.Group.CreateGroup(strGroupName="Cube_2(50)-G0003", crlTargets=[Face(50)])
        Connections.Contacts.TSSS.ContactTable(strName="C0002_Cube_3-G0004_Cube_2-G0003", 
            sunshineContact=SUNSHINE_CONTACT(
                dERROR=0.001, 
                dFRIC=DFLT_DBL, 
                dSLIDE=DFLT_DBL, 
                iICOORD=1, 
                dSFACT=DFLT_DBL, 
                dSFACTT=DFLT_DBL), 
            crplTarget=[CursorPair(Group(3), Group(4))], iColor=65280)
        
        # Get the information of all existing contacts
        listDContacts=JPT.GetAllContacts() 
        JPT.Debugger(listDContacts)
        
        # Print all the related information of each existing contact 
        for contact in listDContacts:
            JPT.Debugger(contact)
        ```
        
        """
        message = "JPT.GetAllContacts({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllCoordinates():
        r"""
        ## Description
        
        Get all the information of all existing coordinate systems.
        
        ## Syntax
        
        ```psj
        JPT.GetAllCoordinates()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[CoordVector](../data-type/psj-utility/pre-utility/built-in-types/CoordVector)_ object or _List of [DCoord](../data-type/psj-utility/pre-utility/built-in-types/DCoord)_ objects containing all the information of all the existing coordinate systems.
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model
        Geometry.Part.Cube(iPartColor=6118844)
        Tools.Coordinates.ThreeNode(crlNodes=[Node(454, 461, 462)])
        Tools.Coordinates.ThreeNode(strName="CRect2", crlNodes=[Node(428, 436, 430)])
        Tools.Coordinates.ThreeNode(strName="CCyl1", iCoordType=1, crlNodes=[Node(457, 474, 473)])
        Tools.Coordinates.ThreeNode(strName="CSph1", iCoordType=2, crlNodes=[Node(316, 340, 333)])
        Tools.Coordinates.ThreeNode(strName="CSph2", iCoordType=2, iOrder=3, crlNodes=[Node(190, 216, 204)])
        JPT.ViewFitToModel()
        
        # Get all the existing coordinate systems
        listDCoords = JPT.GetAllCoordinates()
        JPT.Debugger(listDCoords)
        
        # Print all the related information of each existing coordinate systems in list
        for coord in listDCoords:
            JPT.Debugger(coord)
        ```
        
        """
        message = "JPT.GetAllCoordinates({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllCustomNoteCollections():
        r"""
        ## Description
        
        Get all the information of all existing custom note collections.
        
        ## Syntax
        
        ```psj
        JPT.GetAllCustomNoteCollections()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[CustomNoteVector](../data-type/psj-utility/pre-utility/built-in-types/CustomNoteVector)_ object or _List of [DCustomNote](../data-type/psj-utility/pre-utility/built-in-types/DCustomNote)_ objects containing all the information of all the existing CustomNotes.
        
        ## Sample Code
        
        ```psj {8}
        # Prepare model
        Geometry.Part.Cube(iPartColor=6409934)
        Tools.CustomNote.Create(
            strNoteName="CustomNote_1", 
            dlNotePosition=[0.0, 0.0, 0.0], 
            strParentName="Collection_1", 
            listContent=["Note 1"], 
            iBackgroundColor=15794160, 
            iOutlineColor=14772545, 
            iArrowColor=16711680, 
            iFontSize=16, 
            iAlignment=1
            )
        Tools.CustomNote.Create(
            strNoteName="CustomNote_2", 
            dlNotePosition=[0.0, 0.0, 0.0], 
            strParentName="Collection_2", 
            listContent=["Note 2"], 
            iFontSize=16, 
            iBackgroundColor=11394815, 
            iOutlineColor=128, 
            iArrowColor=3937500, 
            iAlignment=1
            )
        Tools.CustomNote.Create(
            strNoteName="CustomNote_3", 
            dlNotePosition=[0.0, 0.0, 0.0], 
            crParentCollection=CustomNoteCollection(2), 
            listContent=["Note 3"], 
            iFontSize=16, bBold=True, 
            iBackgroundColor=14480885, 
            iOutlineWidth=2, 
            iOutlineColor=25600, 
            iArrowColor=9498256, 
            iArrowType=0
            )
        JPT.DisableScreenAnimation()
        JPT.ViewFitToModel()
        JPT.Exec('ViewSpreadNote()')
        
        # Get the information of all existing Custom Notes
        listDCustomNoteCollections = JPT.GetAllCustomNoteCollections()
        JPT.Debugger(listDCustomNoteCollections)
        
        # Print all the related information of each existing custom note in list
        for custom_note in listDCustomNoteCollections:
            JPT.Debugger(custom_note)
        ```
        
        """
        message = "JPT.GetAllCustomNoteCollections({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllCustomNotes():
        r"""
        ## Description
        
        Get all the information of all existing custom notes.
        
        ## Syntax
        
        ```psj
        JPT.GetAllCustomNotes()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[CustomNoteVector](../data-type/psj-utility/pre-utility/built-in-types/EdgeVector)_ object or _List of [DCustomNote](../data-type/psj-utility/pre-utility/built-in-types/DCustomNote)_ objects containing all the information of all the existing custom notes.
        
        ## Sample Code
        
        ```psj {42}
        # Prepare model
        Geometry.Part.Cube(iPartColor=6409934)
        Tools.CustomNote.Create(
            strNoteName="CustomNote_1", 
            dlNotePosition=[0.0, 0.0, 0.0], 
            strParentName="Collection_1", 
            listContent=["Note 1"], 
            iBackgroundColor=15794160, 
            iOutlineColor=14772545, 
            iArrowColor=16711680, 
            iFontSize=16, 
            iAlignment=1
            )
        Tools.CustomNote.Create(
            strNoteName="CustomNote_2", 
            dlNotePosition=[0.0, 0.0, 0.0], 
            crParentCollection=CustomNoteCollection(1), 
            listContent=["Note 2"], 
            iFontSize=16, 
            iBackgroundColor=11394815, 
            iOutlineColor=128, 
            iArrowColor=3937500, 
            iAlignment=1
            )
        Tools.CustomNote.Create(
            strNoteName="CustomNote_3", 
            dlNotePosition=[0.0, 0.0, 0.0], 
            crParentCollection=CustomNoteCollection(1), 
            listContent=["Note 3"], 
            iFontSize=16, bBold=True, 
            iBackgroundColor=14480885, 
            iOutlineWidth=2, 
            iOutlineColor=25600, 
            iArrowColor=9498256, 
            iArrowType=0
            )
        JPT.DisableScreenAnimation()
        JPT.ViewFitToModel()
        JPT.Exec('ViewSpreadNote()')
        
        # Get the information of all existing Custom Notes
        listDCustomNotes = JPT.GetAllCustomNotes()
        JPT.Debugger(listDCustomNotes)
        
        # Print all the related information of each existing custom note in list
        for custom_note in listDCustomNotes:
            JPT.Debugger(custom_note)
        ```
        
        """
        message = "JPT.GetAllCustomNotes({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllEdges():
        r"""
        ## Description
        
        Get all the information of all existing edges.
        
        ## Syntax
        
        ```psj
        JPT.GetAllEdges()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        An _[EdgeVector](../data-type/psj-utility/pre-utility/built-in-types/EdgeVector)_ object or _List of [DEdge](../data-type/psj-utility/pre-utility/built-in-types/DEdge)_ objects containing all the information of all the existing edges.
        
        ## Sample Code
        
        ```psj {8}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Get the information of all existing edges
        listDEdges = JPT.GetAllEdges()
        JPT.Debugger(listDEdges)
        
        # Print all the related information of each existing edge in list
        for edge in listDEdges:
            JPT.Debugger(edge)
        ```
        
        """
        message = "JPT.GetAllEdges({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllElems():
        r"""
        ## Description
        
        Get all the information of all existing elements.
        
        :::note
        
        If this function is executed on a Post document, it returns 0. If you want to get all Post elements, please use  _[GetAllPostElems](JPT.GetAllPostElems)_. 
        
        :::
        
        ## Syntax
        
        ```psj
        JPT.GetAllElems()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        An _[ElemVector](../data-type/psj-utility/pre-utility/built-in-types/ElemVector)_ object or _List of [DElem](../data-type/psj-utility/pre-utility/built-in-types/DElem)_ objects containing all the information of all the existing elements.
        
        ## Sample Code
        
        ```psj {8}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Get the information of all existing elements
        listDElems = JPT.GetAllElems()
        JPT.Debugger(listDElems)
        
        # Print all the related information of each existing element in list
        for elem in listDElems:
            JPT.Debugger(elem)
        ```
        
        """
        message = "JPT.GetAllElems({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllFaces():
        r"""
        ## Description
        
        Get all the information of all existing faces.
        
        ## Syntax
        
        ```psj
        JPT.GetAllFaces()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[FaceVector](../data-type/psj-utility/pre-utility/built-in-types/FaceVector)_ object or _List of [DFace](../data-type/psj-utility/pre-utility/built-in-types/DFace)_ objects containing all the information of all the existing faces.
        
        ## Sample Code
        
        ```psj {8}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Get the information of all existing faces
        listDFaces = JPT.GetAllFaces()
        JPT.Debugger(listDFaces)
        
        # Print all the related information of each existing face in list
        for face in listDFaces:
            JPT.Debugger(face)
        ```
        
        """
        message = "JPT.GetAllFaces({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllFieldData():
        r"""
        ## Description
        
        Get all the field data inside a document.
        
        ## Syntax
        
        ```psj
        JPT.GetAllFieldData()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[FieldDataVector](../data-type/psj-utility/pre-utility/built-in-types/FieldDataVector)_ object or _List of [DFieldData](../data-type/psj-utility/pre-utility/built-in-types/DFieldData)_ objects containing all the information of all the existing field data.
        
        ## Sample Code
        
        ```psj {19}
        # Prepare data
        BoundaryConditions.FieldData(
            strName="TimeTable",
            iType=2,
            ilSheet=[4, 2, 0, 0, 0.1, 10, 5, 50, 10, 70])
        
        BoundaryConditions.FieldData(
            strName="FreqTable",
            iType=4,
            ilSheet=[3, 2, 1000, 100, 2000, 110, 3000, 120])
        
        BoundaryConditions.FieldData(
            strName="TemparatureTable",
            iType=7,
            ilSheet=[3, 2, 0, 0.1, 100, 0.3, 300, 0.5])
        
        
        # Get the information of all existing field data
        listDFieldData = JPT.GetAllFieldData()
        JPT.Debugger(listDFieldData)
        
        # Print all the related information of each existing field data in list
        for fieldData in listDFieldData:
            JPT.Debugger(fieldData)
        ```
        
        """
        message = "JPT.GetAllFieldData({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllGridMeshInfo(targetFaces, MeshSize, bMerge=0):
        r"""
        ## Description
        
        Get all the gridmesh information for the specified face(s).
        
        ## Syntax
        
        ```psj
        JPT.GetAllGridMeshInfo()
        ```
        
        ## Inputs
        
        ### `targetFaces`
        
        - A _List of Integer_ specifying the ID of target face(s).
        - This is a required input.
        
        ### `MeshSize`
        
        - A _Double_ specifying the mesh size.
        - This option can be left blank. If it is left blank, the function will automatically calculate the mesh size based on the mesh count of all edges of the specified face(s).
        
        ### `bMerge`
        
        - A _Boolean_ specifying whether to merge all specified faces into one face. 
        - The default value is 0.
        
        ## Return Code
        
        A _Dictionary_ specifying the gridmesh information for the specified face(s).
        
        ## Sample Code
        
        ```psj {3}
        Geometry.Part.Cube()
        
        gridmesh_info = JPT.GetAllGridMeshInfo([24,26],0.005,0)
        pprint(gridmesh_info)
        
        # GRIDMESH class information of all specified faces
        print(gridmesh_info['information'])
        
        # GRIDMESH class information of the 1st specified face
        print(gridmesh_info['information'][0])
        
        # Grid mesh count of all specified faces
        print(gridmesh_info['mesh_count'])
        
        # Grid mesh count of the 1st specified face
        print(gridmesh_info['mesh_count'][0])
        
        # Corner nodes of all specified faces
        print(gridmesh_info['corner_node'])
        
        # Corner nodes of the 1st specified face
        print(gridmesh_info['corner_node'][0])
        
        # Target Face
        print(gridmesh_info['target_face'])
        
        # Shape Type
        print(gridmesh_info['shape_type'])
        
        # Element Type
        print(gridmesh_info['elem_type'])
        
        # Optimize status
        print(gridmesh_info['optimize'])
        ```
        """
        message = "JPT.GetAllGridMeshInfo({},{},{})".format(targetFaces,MeshSize,bMerge)
        return JPT_RUN_LINE(message)

    def GetAllGroups():
        r"""
        ## Description
        
        Get all the information of all existing groups.
        
        ## Syntax
        
        ```psj
        JPT.GetAllGroups()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[GroupVector](../data-type/psj-utility/pre-utility/built-in-types/GroupVector)_ object or _List of [DGroup](../data-type/psj-utility/pre-utility/built-in-types/DGroup)_ objects containing all the information of all the existing groups.
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        Tools.Group.CreateGroup(strGroupName="Group1", crlTargets=[Part(1)])
        Tools.Group.CreateGroup(strGroupName="Group2", crlTargets=[Face(47, 48, 49, 50, 51, 52)])
        Tools.Group.CreateGroup(strGroupName="Group3", crlTargets=[Elem(2784, 2296, 2677, 2295, 3144, 2977)])
        JPT.ViewFitToModel()
        
        # Get the information of all existing groups
        listDGroups = JPT.GetAllGroups()
        JPT.Debugger(listDGroups)
        
        # Print all the related information of each existing group in list
        for group in listDGroups:
            JPT.Debugger(group)
        ```
        
        """
        message = "JPT.GetAllGroups({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllLibraryMaterials():
        r"""
        ## Description
        
        Get all the information of all library materials.
        
        ## Syntax
        
        ```psj
        JPT.GetAllLibraryMaterials()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[MaterialLibVector](../data-type/psj-utility/pre-utility/built-in-types/MaterialLibVector)_ object or _List of [DMaterialLib](../data-type/psj-utility/pre-utility/built-in-types/DMaterial)_ objects containing all the information of all the existing user materials.
        
        ## Sample Code
        
        ```psj {11}
        # Get all library materials
        libMat = JPT.GetAllLibraryMaterials()
        print(f"There are {len(libMat)} materials in the library")
        JPT.Debugger(libMat)
        JPT.Debugger(libMat[0])
        ```
        
        """
        message = "JPT.GetAllLibraryMaterials({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllLicensesStatus():
        r"""
        ## Description
        
        Get all available licenses status.
        
        ## Syntax
        
        ```psj
        JPT.GetAllLicensesStatus()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _Dictionary_ stores pairs of license name and its status
        
        ## Sample Code
        
        ```psj {2}
        # Check the status of all available licenses
        pprint(JPT.GetAllLicensesStatus())
        ```
        
        """
        message = "JPT.GetAllLicensesStatus({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllLoadBoundaryConditions():
        r"""
        ## Description
        
        Get all the information of all existing loads and boundary conditions.
        
        ## Syntax
        
        ```psj
        JPT.GetAllLoadBoundaryConditions()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[LoadBCVector](../data-type/psj-utility/pre-utility/built-in-types/LoadBCVector)_ object or _List of [DLoadBC](../data-type/psj-utility/pre-utility/built-in-types/DLoadBC)_ objects containing all the information of all the existing loads and boundary conditions.
        
        ## Sample Code
        
        ```psj {10}
        # Prepare model
        Geometry.Part.Cube(iPartColor=6409934)
        Geometry.Part.Cube(dlOrigin=[0.012, 0.0, 0.0], strName="Cube_2", iPartColor=13259210)
        Geometry.Part.Cube(dlOrigin=[0.024, 0.0, 0.0], strName="Cube_3", iPartColor=7697908)
        BoundaryConditions.FixedConstraint(crlTargets=[Face(76)])
        BoundaryConditions.Pressure.General(crlTargets=[Face(52)])
        JPT.ViewFitToModel()
        
        # Get the information of all existing loads and boundary conditions
        listDLoadBCs = JPT.GetAllLoadBoundaryConditions()
        JPT.Debugger(listDLoadBCs)
        
        # Print all the related information of each existing load/boundary condition in list
        for lbc in listDLoadBCs:
            JPT.Debugger(lbc)
        ```
        
        """
        message = "JPT.GetAllLoadBoundaryConditions({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllLoadsBCs():
        r"""
        ## Description
        
        Get all the information of all existing loads and boundary conditions under _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ format.
        
        ## Syntax
        
        ```psj
        JPT.GetAllLoadsBCs()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing all the information of all the existing loads and boundary conditions.
        
        ## Sample Code
        
        ```psj {10}
        # Prepare model
        Geometry.Part.Cube(iPartColor=6409934)
        Geometry.Part.Cube(dlOrigin=[0.012, 0.0, 0.0], strName="Cube_2", iPartColor=13259210)
        Geometry.Part.Cube(dlOrigin=[0.024, 0.0, 0.0], strName="Cube_3", iPartColor=7697908)
        BoundaryConditions.FixedConstraint(crlTargets=[Face(76)])
        BoundaryConditions.Pressure.General(crlTargets=[Face(52)])
        JPT.ViewFitToModel()
        
        # Get the information of all existing loads and boundary conditions
        listDItemLoadBCs = JPT.GetAllLoadsBCs()
        JPT.Debugger(listDItemLoadBCs)
        
        # Print all the related information of each existing load/boundary condition in list
        for lbc in listDItemLoadBCs:
            JPT.Debugger(lbc)
        ```
        
        """
        message = "JPT.GetAllLoadsBCs({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllMaterials():
        r"""
        ## Description
        
        Get all the information of all existing user materials.
        
        ## Syntax
        
        ```psj
        JPT.GetAllMaterials()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[MaterialVector](../data-type/psj-utility/pre-utility/built-in-types/MaterialVector)_ object or _List of [DMaterial](../data-type/psj-utility/pre-utility/built-in-types/DMaterial)_ objects containing all the information of all the existing user materials.
        
        ## Sample Code
        
        ```psj {11}
        # Prepare Post model
        samplePath = JPT.GetProgramPath() + "SampleData\\Post\\Static_Renkon.op2"
        Home.ImportResults.Nastran(strPath= samplePath, dFaceAngle=60.16, dEdgeAngle=60.16, bReadLoadAndConstraint=True, 
                                    bReadConnection=True, bCreateResultsAtMidNode=True)
        # Convert to Pre
        data = Tools.ToPre(strName="Static_Renkon", ilOptions=[0, 1, 2, 3, 4])
        JPT.SetActiveDocumentByName("Static_Renkon_Converted_Pre",1)
        # Get all user materials
        userMat = JPT.GetAllMaterials()
        JPT.Debugger(userMat)
        JPT.Debugger(userMat[0])
        ```
        
        """
        message = "JPT.GetAllMaterials({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllMeasureNoteCollections():
        r"""
        ## Description
        
        Get all the information of all existing measure note collections.
        
        ## Syntax
        
        ```psj
        JPT.GetAllMeasureNoteCollections()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[MeasureNoteVector](../data-type/psj-utility/pre-utility/built-in-types/MeasureNoteVector)_ object or _List of [DMeasureNote](../data-type/psj-utility/pre-utility/built-in-types/DMeasureNote)_ objects containing all the information of all the existing edges.
        
        ## Sample Code
        
        ```psj {25}
        # Prepare model
        Geometry.Part.Cube(iPartColor=6409934)
        
        Tools.Measure.Angle.CreateMeasureNote.ThreeNodes(
            strNoteName="Angle_1", 
            crFirstNode=Node(472), 
            crSecondNode=Node(83), 
            crThirdNode=Node(447)
            )
        
        Tools.Measure.Area.CreateMeasureNote.Element(
            strNoteName="Area_1", 
            crlElements=[Elem(1001)]
            )
        
        Tools.Measure.Radius.CreateMeasureNote.ThreeNodes(
            strNoteName="Radius_1", 
            crFirstNode=Node(189), 
            crSecondNode=Node(191), 
            crThirdNode=Node(216)
            )
        
        JPT.ViewFitToModel()
        
        listDMeasureNoteCollections = JPT.GetAllMeasureNoteCollections()
        JPT.Debugger(listDMeasureNoteCollections)
        
        ```
        
        """
        message = "JPT.GetAllMeasureNoteCollections({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllMeasureNotes():
        r"""
        ## Description
        
        Get all the information of all existing custom notes.
        
        ## Syntax
        
        ```psj
        JPT.GetAllMeasureNotes()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        An _[MeasureNoteVector](../data-type/psj-utility/pre-utility/built-in-types/MeasureNotevector)_ object or _List of [DMeasureNote](../data-type/psj-utility/pre-utility/built-in-types/DMeasureNote)_ objects containing all the information of all the existing custom notes.
        
        ## Sample Code
        
        ```psj {21}
        # Prepare model
        Geometry.Part.Cube(iPartColor=6409934)
        Tools.Measure.Distance.CreateMeasureNote.TwoNodes(
            strNoteName="Distance_1", 
            crFirstNode=Node(250), 
            crSecondNode=Node(261)
            )
        Tools.Measure.Distance.CreateMeasureNote.TwoNodes(
            strNoteName="Distance_1", 
            crFirstNode=Node(257), 
            crSecondNode=Node(291)
            )
        Tools.Measure.Angle.CreateMeasureNote.ThreeNodes(
            strNoteName="Angle_1", 
            crFirstNode=Node(441), 
            crSecondNode=Node(438), 
            crThirdNode=Node(475)
            )
        
        # Get the information of all existing measure notes
        listDMeasureNotes = JPT.GetAllMeasureNotes()
        JPT.Debugger(listDMeasureNotes)
        
        # Print all the related information of each existing measure notes in list
        for measure_note in listDMeasureNotes:
            JPT.Debugger(measure_note)
        ```
        
        """
        message = "JPT.GetAllMeasureNotes({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllNodes():
        r"""
        ## Description
        
        Get all the information of all existing nodes.
        
        
        :::note
        
        If this function is executed on a Post document, it returns 0. If you want to get all Post nodes, please use  _[GetAllPostNodes](JPT.GetAllPostNodes)_. 
        
        :::
        
        ## Syntax
        
        ```psj
        JPT.GetAllNodes()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[NodeVector](../data-type/psj-utility/pre-utility/built-in-types/NodeVector)_ object or _List of [DNode](../data-type/psj-utility/pre-utility/built-in-types/DNode)_ objects containing all the information of all the existing nodes.
        
        ## Sample Code
        
        ```psj {8}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Get the information of all existing nodes
        listDNodes = JPT.GetAllNodes()
        JPT.Debugger(listDNodes)
        
        # Print all the related information of each existing node in list
        for node in listDNodes:
            JPT.Debugger(node)
        ```
        
        """
        message = "JPT.GetAllNodes({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllParts():
        r"""
        ## Description
        
        Get all the information of all existing parts.
        
        ## Syntax
        
        ```psj
        JPT.GetAllParts()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[BodyVector](../data-type/psj-utility/pre-utility/built-in-types/BodyVector)_ object or _List of [DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_ objects containing all the information of all the existing parts.
        
        ## Sample Code
        
        ```psj {8}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Get the information of all existing parts
        listDBodies = JPT.GetAllParts()
        JPT.Debugger(listDBodies)
        
        # Print all the related information of each existing part in list
        for part in listDBodies:
            JPT.Debugger(part)
        ```
        
        """
        message = "JPT.GetAllParts({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllPartsInSubAssembly(subAssem):
        r"""
        ## Description
        
        Get all the information of all parts under the inputted sub-assembly.
        
        ## Syntax
        
        ```psj
        JPT.GetAllPartsInSubAssembly(subAssem)
        ```
        
        ## Inputs
        
        ### `subAssem`
        
        - A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object specifying the inputted sub-assembly.
        - This is a required input.
        
        ## Return Code
        
        A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects specifying the parts belonging to the inputted sub-assembly.
        
        ## Sample Code
        
        ```psj {16}
        # Prepare model
        Geometry.Part.Cube(iPartColor=15426917)
        Geometry.Part.Cube(strName="Cube_2", iPartColor=13390932)
        Geometry.Part.Cube(strName="Cube_3", iPartColor=16448103)
        Geometry.Part.Cube(strName="Cube_4", iPartColor=13619046)
        Geometry.Part.Cube(strName="Cube_5", iPartColor=7861111)
        JPT.ViewFitToModel()
        Assembly.RightClick.AddSubAssembly()
        
        # Copy all parts to the created Subassembly
        currentDoc = JPT.GetActiveDocument()
        Assembly.RightClick.TransferDocumentData(strSourceDocTitle=currentDoc.docName, 
                                                strDestDocTitle=currentDoc.docName, 
                                                crlParts=[Part(part.id) for part in JPT.GetAllParts()], 
                                                strlNewPartName=[], 
                                                crDestAssemblyInstance=Inst(1))
        
        # Get the information of all parts belonging to the inputted sub-assembly
        listPartsInSubAssembly = JPT.GetAllPartsInSubAssembly(JPT.FindSubAssemblyByID(1))
        JPT.Debugger(listPartsInSubAssembly)
        ```
        
        """
        message = "JPT.GetAllPartsInSubAssembly({})".format(subAssem)
        return JPT_RUN_LINE(message)

    def GetAllPostElems():
        r"""
        ## Description
        
        Get all the information of all existing Post (read-only) elements.
        
        :::note
        
        If this function is executed on a Pre document, it returns 0. If you want to get all pre elements, please use  _[GetAllElems](JPT.GetAllElems)_. 
        
        :::
        
        ## Syntax
        
        ```psj
        JPT.GetAllPostElems()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        An _[PostElemVector](../data-type/psj-utility/post-utility/post-built-in-types/PostNodeVector)_ object or _List of [DPostElem](../data-type/psj-utility/post-utility/post-built-in-types/DPostElem)_ objects containing all the information of all the existing elements.
        
        ## Sample Code
        
        ```psj {12}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XX, 4}, \
                                    {2, 1, 0, 0, 1, 0, 0, 0.000000, 0}, 0, \
                                    {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, \
                                    0, {0, 0, 0, 0, , , 0}, \
                                    {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')
        
        # Get the result values of Elements
        for postElem in JPT.GetAllPostElems():
            value=JPT.GetResultByElemId(postElem.id)
            print(f"Stress of XX component of Element ID = {postElem.id}:{value}")
        ```
        
        """
        message = "JPT.GetAllPostElems({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllPostFreqResponses():
        r"""
        ## Description
        
        Get all the information of all existing frequency responses.
        
        ## Syntax
        
        ```psj
        JPT.GetAllPostFreqResponses()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[DPostResponse](../data-type/psj-utility/post-utility/post-built-in-types/DPostResponse)_ objects containing all the information of all the existing Frequency responses.
        
        ## Sample Code
        
        ```psj {23}
        # Prepare result model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate_eigen.op2"
        Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16) 
        
        # Create a load condition
        Calculation.FreqResp.LoadCondition(strName="FRQLoad_1", iLoadDirection=2, dlForce=[0.0, 0.0, 10.0], 
                                            dAmplitude=10.0, crlTargets=[Node(1516)]) 
        
        # Create a load case
        Calculation.FreqResp.LoadCaseCondition(crTargetAnalysis=PostFreqAnalysis(1), strName="LoadCase_1", 
                                        crlSelectedLoad=[PostFreqLoad(1)], dlTargetFactor=[1.0])
        
        # Create a response condition
        respCondition = Calculation.FreqResp.ResponseCondition(crTargetAnalysis=PostFreqAnalysis(1), 
                                                                dDampingFactor=0.02, dStyleParamMid=10.0, 
                                                                dStyleParamBot=200.0, strlResultNames=["TZ"], 
                                                                crlTargets=[Node(1516, 1016)])
        Chart.CreateGraph(crTargetCurve=PostFreqResultCurve(1), strChartTitle="Frequency Analysis Displacement", 
                        strAxisTitleX="Frequency", strAxisTitleY="Amplitude", bNewChart=False)
        Chart.CreateGraph(crTargetCurve=PostFreqResultCurve(3), strChartTitle="Frequency Analysis Displacement", 
                        strAxisTitleX="Frequency", strAxisTitleY="Amplitude", bNewChart=False)
        # Get all Post Frequency Response
        listResponses = JPT.GetAllPostFreqResponses()
        JPT.Debugger(listResponses)
        for response in listResponses:
            print(response.name)
            print(response.type)
            print(response.id)
            JPT.Debugger(response.targetAnalysis)
            JPT.Debugger(response.resultCurve)
        ```
        
        """
        message = "JPT.GetAllPostFreqResponses({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllPostFreqResponseSolvers():
        r"""
        ## Description
        
        Get all the information of all existing Frequency responses (solver).
        
        ## Syntax
        
        ```psj
        JPT.GetAllPostFreqResponseSolvers()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[DPostResponse](../data-type/psj-utility/post-utility/post-built-in-types/DPostResponse)_ objects containing all the information of all the existing Frequency Responses (Solver).
        
        ## Sample Code
        
        ```psj {29}
        # Prepare result model
        inputPath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Command\\PostSample\\freq-solver\\103.bdf"
        outputFolder = "C:\\temp"
        JPT.RunSunShine(inputPath,outputFolder,2,1,False,True,False)
        
        Home.ImportResults.Nastran(strPath = outputFolder + "\\103.op2", dFaceAngle=60.16, dEdgeAngle=60.16) 
        
        # Create Frequency Analysis Load - Solver
        Calculation.FreqRespSolver.LoadCondition(strName="FRQLoad_1", 
                                                iLoadDirection=2, 
                                                dlForce=[0.0, 0.0, 10.0], 
                                                dAmplitude=10.0, 
                                                crlTargets=[Node(514)])
        
        # Create Frequency Analysis Transient - Solver
        respCondition = Calculation.FreqRespSolver.ResponseCondition(crTargetAnalysis=PostFreqAnalysisSolver(1), 
                                                                    bDampingFactor=False, 
                                                                    dDampingFactor=0.02, 
                                                                    iCurveStyle=2, 
                                                                    dStyleParamMid=20.0, 
                                                                    dStyleParamBot=50000.0, 
                                                                    strlResultNames=["TZ"], 
                                                                    strDBFileName="103", 
                                                                    strDBVersion="1", 
                                                                    strMethodId="2", 
                                                                    strPath="C:/temp/113.bdf", 
                                                                    crlTargets=[Node(517)])
        # Get all Post Frequency Response (Solver)
        listResponses = JPT.GetAllPostFreqResponseSolvers()
        JPT.Debugger(listResponses)
        for response in listResponses:
            print(response.name)
            print(response.type)
            print(response.id)
            JPT.Debugger(response.targetAnalysis)
            JPT.Debugger(response.resultCurve)
        ```
        """
        message = "JPT.GetAllPostFreqResponseSolvers({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllPostGururiResponse():
        r"""
        ## Description
        
        Get all the information of all existing Grururi responses.
        
        ## Syntax
        
        ```psj
        JPT.GetAllPostGururiResponses()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[DPostResponse](../data-type/psj-utility/post-utility/post-built-in-types/DPostResponse)_ object containing all the information of all the existing Grururi responses.
        
        ## Sample Code
        
        ```psj {19}
        # Please set path to your result sample file
        samplePath = "C:/Temp/Sample.op2"
        
        # Prepare result model
        Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60, dEdgeAngle=60)
        
        # Create a load condition
        Calculation.Gururi.LoadCondition(strName="FRQLoad_1", iLoadDirection=2, dlForce=[0.0, 0.0, 10.0], 
                                        dAmplitude=10.0, crlTargets=[Node(501)])
        
        # Create a load case
        loadCase = Calculation.Gururi.LoadCase(crTargetAnalysis=PostFreqAnalysis(1), strName="LoadCase_1", 
                                                crlSelectedLoad=[PostFreqLoad(1)], dlTargetFactor=[1.0])
        
        # Response calculation
        response = Calculation.Gururi.Response(crTargetAnalysis=PostFreqAnalysis(1), dInputFrequency=180.0, 
                                                iStepNumber=30)
        # Get all Post Gururi Response
        listResponses = JPT.GetAllPostFreqResponsesSolver()
        JPT.Debugger(listResponses)
        for response in listResponses:
            print(response.name)
            print(response.type)
            print(response.id)
            JPT.Debugger(response.targetAnalysis)
        ```
        
        """
        message = "JPT.GetAllPostGururiResponse({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllPostNodes():
        r"""
        ## Description
        
        Get all the information of all existing Post (read-only) nodes.
        
        :::note
        
        If this function is executed on a Pre document, it returns 0. If you want to get all pre nodes, please use  _[GetAllNodes](JPT.GetAllNodes)_. 
        
        :::
        
        ## Syntax
        
        ```psj
        JPT.GetAllPostNodes()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[PostNodeVector](../data-type/psj-utility/post-utility/post-built-in-types/PostNodeVector)_ object or _List of [DPostNode](../data-type/psj-utility/post-utility/post-built-in-types/DPostNode)_ objects containing all the information of all the existing nodes.
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Displacement, X, 1}, {1, 1, 0, \
                                     0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, \
                                     {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, \
                                     {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')
        
        # Get the result values of Nodes
        for postNode in JPT.GetAllPostNodes():
            value=JPT.GetResultByNodeId(postNode.id)
            print(f"Displacement of X component of Node ID = {postNode.id}:{value}")
        ```
        
        """
        message = "JPT.GetAllPostNodes({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllPostResultCurves():
        r"""
        ## Description
        
        Get all the information of all existing Post result curves.
        
        ## Syntax
        
        ```psj
        JPT.GetAllPostResultCurves()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[DPostResultCurve](../data-type/psj-utility/post-utility/post-built-in-types/DPostResultCurve)_ object containing all the information of all the existing Post result curves.
        
        ## Sample Code
        
        ```psj {23}
        # Prepare result model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate_eigen.op2"
        Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16) 
        
        # Create a load condition
        Calculation.FreqResp.LoadCondition(strName="FRQLoad_1", iLoadDirection=2, dlForce=[0.0, 0.0, 10.0], 
                                            dAmplitude=10.0, crlTargets=[Node(1516)]) 
        
        # Create a load case
        Calculation.FreqResp.LoadCaseCondition(crTargetAnalysis=PostFreqAnalysis(1), strName="LoadCase_1", 
                                        crlSelectedLoad=[PostFreqLoad(1)], dlTargetFactor=[1.0])
        
        # Create a response condition
        respCondition = Calculation.FreqResp.ResponseCondition(crTargetAnalysis=PostFreqAnalysis(1), 
                                                                dDampingFactor=0.02, dStyleParamMid=10.0, 
                                                                dStyleParamBot=200.0, strlResultNames=["TZ"], 
                                                                crlTargets=[Node(1516, 1016)])
        Chart.CreateGraph(crTargetCurve=PostFreqResultCurve(1), strChartTitle="Frequency Analysis Displacement", 
                        strAxisTitleX="Frequency", strAxisTitleY="Amplitude", bNewChart=False)
        Chart.CreateGraph(crTargetCurve=PostFreqResultCurve(3), strChartTitle="Frequency Analysis Displacement", 
                        strAxisTitleX="Frequency", strAxisTitleY="Amplitude", bNewChart=False)
        # Get all Post result curves
        listCurves = JPT.GetAllPostResultCurves()
        JPT.Debugger(listCurves)
        for curve in listCurves:
            if "MPF" not in curve.name:
                print(curve.name)
                print(curve.rowCount)
                print(curve.colCount)
                print(curve.typeID)
                print(curve.curveType)
                JPT.Debugger(curve.allData)
                JPT.Debugger(curve.frequency)
                JPT.Debugger(curve.amplitude)
                JPT.Debugger(curve.phase)
                JPT.Debugger(curve.real)
                JPT.Debugger(curve.imagine)
            else:
                print(curve.name)
                print(curve.rowCount)
                print(curve.colCount)
                print(curve.typeID)
                print(curve.curveType)
        ```
        
        """
        message = "JPT.GetAllPostResultCurves({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllPostTransResponses():
        r"""
        ## Description
        
        Get all the information of all existing Transient responses.
        
        ## Syntax
        
        ```psj
        JPT.GetAllPostTransResponses()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[DPostResponse](../data-type/psj-utility/post-utility/post-built-in-types/DPostResponse)_ object containing all the information of all the existing Transient responses.
        
        ## Sample Code
        
        ```psj {23}
        # Prepare result model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate_eigen.op2"
        Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
        
        # Create a load condition
        Calculation.TransResp.LoadCondition(strName="TRNLoad_2", iLoadType=1, iLoadDirection=2, 
                                            dlForce=[0.0, 0.0, 10.0], dAmplitude=10, dT1=0.1, dT2=0.5, 
                                            dFrequency=10.0, crlTargets=[Node(1516)])
        
        # Create a loadcase
        Calculation.TransResp.LoadCaseCondition(crTargetAnalysis=PostTransAnalysis(1), strName="LoadCase_1",
                                                crlSelectedLoad=[PostTransLoad(1)], dlTargetFactor=[1.0])
        
        # Create response condition
        respCondition = Calculation.TransResp.ResponseCondition(crTargetAnalysis=PostTransAnalysis(1), dDampingFactor=0.02, 
                                                                iCurveStyle=0, dStyleParamMid=80.0, dStyleParamBot=0.0125, 
                                                                strlResultNames=["TZ"], crlTargets=[Node(1516, 1016)])
        Chart.CreateGraph(crTargetCurve=PostTransResultCurve(1), strChartTitle="Transient Analysis Displacement", 
                        strAxisTitleX="Time", strAxisTitleY="Data")
        Chart.CreateGraph(crTargetCurve=PostTransResultCurve(3), strChartTitle="Transient Analysis Displacement", 
                        strAxisTitleX="Time", strAxisTitleY="Data", bNewChart=False)
        # Get all Post Transient Response
        listResponses = JPT.GetAllPostTransResponses()
        JPT.Debugger(listResponses)
        for response in listResponses:
            print(response.name)
            print(response.type)
            print(response.id)
            JPT.Debugger(response.targetAnalysis)
            JPT.Debugger(response.resultCurve)
        ```
        
        """
        message = "JPT.GetAllPostTransResponses({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllPostTransResponseSolvers():
        r"""
        ## Description
        
        Get all the information of all existing Transient responses (Solver).
        
        ## Syntax
        
        ```psj
        JPT.GetAllPostTransResponseSolvers()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[DPostResponse](../data-type/psj-utility/post-utility/post-built-in-types/DPostResponse)_ object containing all the information of all the existing Transient Responses (Solver).
        
        ## Sample Code
        
        ```psj {29}
        # Prepare result model
        inputPath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Command\\PostSample\\freq-solver\\103.bdf"
        outputFolder = "C:\\temp"
        JPT.RunSunShine(inputPath,outputFolder,2,1,False,True,False)
        
        Home.ImportResults.Nastran(strPath = outputFolder + "\\103.op2", dFaceAngle=60.16, dEdgeAngle=60.16) 
        
        # Create Transient Analysis Load - Solver
        Calculation.TransRespSolver.LoadCondition(strName="TRNLoad_1", 
                                                iLoadDirection=2, 
                                                dlForce=[0.0, 0.0, 10.0], 
                                                dAmplitude=10.0, 
                                                crlTargets=[Node(514)])
        
        # Create Transient Analysis Response - Solver
        respCondition = Calculation.TransRespSolver.ResponseCondition(crTargetAnalysis=PostTransAnalysisSolver(1), 
                                                                    bDampingFactor=False, 
                                                                    dDampingFactor=0.02, 
                                                                    iCurveStyle=2, 
                                                                    dStyleParamMid=20.0, 
                                                                    dStyleParamBot=5000.0, 
                                                                    strlResultNames=["TZ"], 
                                                                    strDBFileName="103", 
                                                                    strDBVersion="1", 
                                                                    strMethodId="2", 
                                                                    strPath="C:/temp/111.bdf", 
                                                                    crlTargets=[Node(517)])
        # Get all Post Transient Response (Solver)
        listResponses = JPT.GetAllPostTransResponseSolvers()
        JPT.Debugger(listResponses)
        for response in listResponses:
            print(response.name)
            print(response.type)
            print(response.id)
            JPT.Debugger(response.targetAnalysis)
            JPT.Debugger(response.resultCurve)
        ```
        
        """
        message = "JPT.GetAllPostTransResponseSolvers({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllResultsByElemId(elementID, bReturnBlank=False):
        r"""
        ## Description
        
        Get all result values of specified Element by ID.
        
        ## Syntax
        
        ```psj
        JPT.GetAllResultsByElemId(elementID,breturnBlank)
        ```
        ## Inputs
        
        ### `elementID`
        
        - An _Integer_ specifying the ID of Element to be checked the result value.
        - This is a required input.
        
        ### `bReturnBlank`
        
        - A _Boolean_ specifying the option to express the blank value. 
        - The default value is False.
        
        ## Return Code
        
        A List specifying all results of Element.
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, Mises, 2}, \
                                    {1, 0, 0, 0, 16, 0, 0, 0.000000, 0}, 0, \
                                    {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, \
                                    {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')
        
        # Get the all result values of Element ID = 33
        valuesElemID = JPT.GetAllResultsByElemId(33)
        for data in valuesElemID:
            type, id, value= data
            print(f'Type:{type} ID:{id} Value:{value}')
        ```
        
        """
        message = "JPT.GetAllResultsByElemId({},{})".format(elementID,bReturnBlank)
        return JPT_RUN_LINE(message)

    def GetAllResultsByNodeId(nodeID, bReturnBlank=False):
        r"""
        ## Description
        
        Get all result values of specified Node by ID.
        
        ## Syntax
        
        ```psj
        JPT.GetAllResultsByNodeId(nodeID)
        ```
        
        ## Inputs
        
        ### `nodeID`
        
        - An _Integer_ specifying the ID of Node to be checked the result value.
        - This is a required input.
        
        ### `bReturnBlank`
        
        - A _Boolean_ specifying the option to express the blank value. 
        - The default value is False.
        
        
        ## Return Code
        
        A List specifying all results of Node.
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XX, 4}, \
                                    {1, 1, 0, 0, 16, 0, 0, 0.000000, 0}, 0, \
                                    {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, \
                                    {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')
        
        # Get the result values of Node ID = 60
        valuesNodeID = JPT.GetAllResultsByNodeId(60)
        for data in valuesNodeID:
            type, id, value= data
            print(f'Type:{type} ID:{id} Value:{value}')
        ```
        
        """
        message = "JPT.GetAllResultsByNodeId({},{})".format(nodeID,bReturnBlank)
        return JPT_RUN_LINE(message)

    def GetAllSelected():
        r"""
        ## Description
        
        Get all the information of all selected entities (Connections, Contacts, Parts, ...).
        
        ## Syntax
        
        ```psj
        JPT.GetAllSelected()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing all the information of all the selected entities.
        
        ## Sample Code
        
        ```psj {13}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Select part
        listIDParts = [part.id for part in JPT.GetAllParts()]
        strIDCursor = " ".join(str(cursor) for cursor in listIDParts)
        Home.Find(strSearch=f"{strIDCursor}", strSelectedType="Part")
        
        #Get the information of all selected parts
        listSelParts = JPT.GetAllSelected()
        JPT.Debugger(listSelParts)
        ```
        
        """
        message = "JPT.GetAllSelected({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllSolverJobs():
        r"""
        ## Description
        
        Get all the information of solver jobs (job name, steps, job description).
        
        ## Syntax
        
        ```psj
        JPT.GetAllSolverJobs()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[SolverJobVector](../data-type/psj-utility/pre-utility/built-in-types/SolverJobVector)_ object or _List of [DSolverJob](../data-type/psj-utility/pre-utility/built-in-types/DSolverJob)_ objects containing all the information of all the jobs.
        
        ## Sample Code
        
        ```psj {7}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\JtdbSample\\Get_Infor_Part_Sample.jtdb"
        FileMenu.LoadJTDB(strFileName=samplePath)
        JPT.ViewFitToModel()
        
        # Get the information of all solver jobs
        listJobs = JPT.GetAllSolverJobs()
        JPT.Debugger(listJobs) #size = 3
        
        # Declare job variables
        ADVC_Job = listJobs[0]
        Abaqus_Job = listJobs[1]
        Nastran_Job = listJobs[2]
        
        # Access Name/Step/Description of ADVC Job
        JPT.Debugger(ADVC_Job)
        JPT.Debugger(ADVC_Job.name)
        JPT.Debugger(ADVC_Job.jobDescription)
        for step in ADVC_Job.jobSteps:
            JPT.Debugger(step)
        
        # Access Name/Step/Description of Abaqus Job
        JPT.Debugger(Abaqus_Job)
        JPT.Debugger(Abaqus_Job.name)
        JPT.Debugger(Abaqus_Job.jobDescription)
        for step in Abaqus_Job.jobSteps:
            JPT.Debugger(step)
        
        # Access Name/Step/Description of Nastran Job
        JPT.Debugger(Nastran_Job)
        JPT.Debugger(Nastran_Job.name)
        JPT.Debugger(Nastran_Job.jobSteps) #size = 0, Nastran does not have steps
        JPT.Debugger(Nastran_Job.jobDescription)
        ```
        
        """
        message = "JPT.GetAllSolverJobs({})".format('')
        return JPT_RUN_LINE(message)

    def GetAllSubGroups():
        r"""
        ## Description
        
        Get all the sub groups information.
        
        ## Syntax
        
        ```psj
        JPT.GetAllSubGroups()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[SubGroupVector](../data-type/psj-utility/pre-utility/built-in-types/SubGrouector)_ object or _List of [DSubGroup](../data-type/psj-utility/pre-utility/built-in-types/DSubGroup)_ objects containing all the information of all the existing elements.
        
        ## Sample Code
        
        ```psj {18}
        # Prepare model
        Geometry.Part.Cube(iPartColor=6409934)
        Tools.Group.CreateGroup(
            strGroupName="Group1", 
            crlTargets=[Face(26, 22)])
        Groups.RightClick.AddSubGroup()
        Groups.RightClick.AddSubGroup()
        Groups.RightClick.CopyGroup(
            crlGroups=[Group(1)], 
            strlNames=["Group1(1)"], 
            crSubGroup=SubGroup(1), bKeepOriginalGroup=True)
        Groups.RightClick.CopyGroup(
            crlGroups=[Group(1)], 
            strlNames=["Group1(2)"], 
            crSubGroup=SubGroup(2), bKeepOriginalGroup=True)
        
        # Get all Sub-groups
        listSubGroups = JPT.GetAllSubGroups()
        JPT.Debugger(listSubGroups)
        
        # Iterate all sub groups of model
        for subGroup in listSubGroups:
            JPT.Debugger(subGroup)    
            # Access id of sub-group
            id = subGroup.id
            JPT.Debugger(id)
            # Access typeID of sub-group
            typeid = subGroup.typeID
            JPT.Debugger(typeid)
            # Access name of sub-group
            name = subGroup.name
            JPT.Debugger(name)
            # Access parent of sub-group
            parent = subGroup.parent
            JPT.Debugger(parent)
            # Access children of sub-group
            children = subGroup.children
            JPT.Debugger(children)
            # Iterate all the children
            for child in children:
                JPT.Debugger(child)
        ```
        
        """
        message = "JPT.GetAllSubGroups({})".format('')
        return JPT_RUN_LINE(message)

    def GetAppPathInfo(PathType):
        r"""
        ## Description
        
        Get all the working path of the current Jupiter program.
        
        ## Syntax
        
        ```psj
        JPT.GetAppPathInfo(PathType)
        ```
        
        ## Inputs
        
        ### `PathType`
        
        - An _Enum_ specifying the _[PathType](../data-type/psj-utility/pre-utility/enumeration-types/path-types)_ describing the type of paths which are available for using.
        - This is a required input.
        
        ## Return Code
        
        A _String_ specifying the path relating to the inputted _[PathType](../data-type/psj-utility/pre-utility/enumeration-types/path-types)_.
        
        ## Sample Code
        
        ```psj {2}
        # Path to the installation folder
        print(JPT.GetAppPathInfo(JPT.PathType.PROGRAM_PATH))
        ```
        
        """
        message = "JPT.GetAppPathInfo({})".format(PathType)
        return JPT_RUN_LINE(message)

    def GetAssemblyEntityData(DItemType, itemID):
        r"""
        ## Description
        
        Get all information of a specific item from Assembly Tree.
        
        ## Syntax
        
        ```psj
        JPT.GetAssemblyEntityData(DItemType,itemID)
        ```
        
        ## Inputs
        
        ### `DItemType`
        
        - An _Enum_ specifying _[DItemType](../data-type/psj-command/DItem-types)_ of the target item.
        - This is a required input.
        
        ### `itemID`
        
        - An _Integer_ specifying the ID of the item.
        - This is a required input.
        
        ## Return Code
        
        A _Dictionary_ specifying the data information of the inputted type.
        
        ## Sample Code
        
        ```psj {12,18,22,26,30,34}
        # Prepare model
        JPT.Exec('CreateCube([0, 0, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube_1", 7105764, 0:0)')
        JPT.Exec('CreateCube([0.02, 0, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube_2", 6409934, 0:0)')
        JPT.Exec('CreateCube([0, 0.02, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube_3", 13259210, 0:0)')
        JPT.Exec('PressureGeneral("Pressure2", 1e+08, 0, 0:0, 0, 0, 0:0, "", 0:0, [1.7976931e+308, 1.7976931e+308, 1.7976931e+308], "", "", "", 1, [6:52], 0:0)')
        JPT.Exec('ForceGeneral("Force2", [-100, 1.7976931e+308, 1.7976931e+308], [1.7976931e+308, 1.7976931e+308, 1.7976931e+308], 0, 0, 0:0, 0:0, 0:0, 0, 0, 0:0, "", "", "", "", "", "", [6:23], 0:0)')
        JPT.Exec('FixedConstraint("Constraint1", 7, 0:0, 0, 0, 0:0, 0, [6:77], 0:0)')
        JPT.Exec('BoundaryTemperature("BoundaryTemperature_1", 293.15, 0:0, [6:78], 0:0)')
        JPT.ViewFitToModel()
        
        # Get information of Cube_1 from assembly tree
        PartDict = JPT.GetAssemblyEntityData(JPT.DItemType.BODY, 1)
        
        # Dump out result
        pprint(PartDict)
        
        # Print out the color of Feature Edge and convert to RGB format
        colorRGB = JPT.ConvertJPTColorToRGB(int(PartDict["Part"]["Surface"]["Colors"]["Feature Edge"]))
        print("Feature Edge Color: " + colorRGB)
        
        # Get information of Boundary Constraint from assembly tree
        ConstraintDict = JPT.GetAssemblyEntityData(JPT.DItemType.LBC_CONSTRAINT, 1)
        pprint(ConstraintDict)
        
        # Get information of Force from assembly tree
        ForceDict = JPT.GetAssemblyEntityData(JPT.DItemType.LBC_FORCE, 2)
        pprint(ForceDict)
        
        # Get information of Pressure from assembly tree
        PressureDict = JPT.GetAssemblyEntityData(JPT.DItemType.LBC_G_PRESSURE, 1)
        pprint(PressureDict)
        
        # Get information of Pressure from assembly tree
        TempDict = JPT.GetAssemblyEntityData(JPT.DItemType.LBC_TEMP_BOUNDARY, 1)
        pprint(TempDict)
        ```
        
        """
        message = "JPT.GetAssemblyEntityData({},{})".format(DItemType,itemID)
        return JPT_RUN_LINE(message)

    def GetAvailableResultOption(PostAnalysisType, resultSet, timeStep, resultName, componentName, PostResultDataLoc, defaultResultOption):
        r"""
        ## Description
        
        Get available result option of the inputted result type.
        
        ## Syntax
        
        ```psj
        JPT.GetAvailableResultOption(PostAnalysisType,
                                     resultSet,
                                     timeStep,
                                     resultName,
                                     componentName,
                                     PostResultDataLoc,
                                     defaultResultOption)
        ```
        
        ## Inputs
        
        ### `PostAnalysisType`
        
        - An _Enum_ specifying the _[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.
        - This is a required input.
        
        ### `resultSet`
        
        - An _Integer_ specifying the step ID of the imported result.
        - This is a required input.
        
        ### `timeStep`
        
        - An _Integer_ specifying the time step of the imported result.
        - This is a required input.
        
        ### `resultName`
        
        - A _String_ specifying the type of result (Such as Displacement, Stress, etc.).
        - This is a required input.
        
        ### `componentName`
        
        - A _String_ specifying a specific direction of the result (Such as X, Y, Z, etc.).
        - This is a required input.
        
        ### `PostResultDataLoc`
        
        - An _Enum_ specifying the _[PostResultDataLoc](../data-type/psj-utility/post-utility/enumeration-types/post-result-data-loc-types)_ describing the location of result (Such as on node, on element, etc.).
        - This is a required input.
        
        ### `defaultResultOption`
        
        - A _[PostDataOp](../data-type/psj-utility/post-utility/post-built-in-types/post-data-op)_ object specifying the default setting of the working result.
        - This is a required input.
        
        ## Return Code
        
        A _[PostDataOp](../data-type/psj-utility/post-utility/post-built-in-types/post-data-op)_ object containing the available setting of the working result.
        
        ## Sample Code
        
        ```psj {5-20}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
        
        available_result_option = \
            JPT.GetAvailableResultOption(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,
                                         1,
                                         1,
                                         "Displacement",
                                         "X",
                                         JPT.PostResultDataLoc.POST_LOC_ON_NODE,
                                         JPT.GetDefaultResultOption(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,
                                                                    1,
                                                                    1,
                                                                    "Displacement",
                                                                    "X",
                                                                    JPT.PostResultDataLoc.POST_LOC_ON_NODE)
                                        )
        
        JPT.Debugger(available_result_option)
        
        # Component of PostDataOp
        print("Location: " + str(available_result_option.loc))
        print("Conversion: " + str(available_result_option.cnv))
        print("Continuously: " + str(available_result_option.cont))
        print("Coordinate: " + str(available_result_option.coord))
        print("Load 1D: " + str(available_result_option.load1d))
        print("Load 2D: " + str(available_result_option.load2d))
        print("Complex: " + str(available_result_option.complex))
        print("Phase Angle: " + str(available_result_option.phaseAngle))
        print("User Coordinate ID: " + str(available_result_option.userCoordSysId))
        ```
        
        <!-- [//]: # "amt is not used in the current version"
        
        [//]: # (print("Amplitude: " + str(available_result_option.amt)) -->
        
        """
        message = "JPT.GetAvailableResultOption({},{},{},{},{},{},{})".format(PostAnalysisType,resultSet,timeStep,resultName,componentName,PostResultDataLoc,defaultResultOption)
        return JPT_RUN_LINE(message)

    def GetCenterOfEntities(DItemVector):
        r"""
        ## Description
        
        Get center coordinate of selected entities.
        
        ## Syntax
        
        ```psj
        JPT.GetCenterOfEntities(DItemVector)
        ```
        
        ## Inputs
        
        ### `DItemVector`
        
        - A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects specifying the targets to get center coordinates.
        - This is a required input.
        
        ## Return Code
        
        A _[DoubleVector](../data-type/psj-utility/pre-utility/built-in-types/DoubleVector)_ object or _List of Double_ value containing the coordinate values \[x, y, z\] of the center of the inputted entities.
        
        ## Sample Code
        
        ```psj {9}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Get the center coordinate of the inputted entities
        listParts = JPT.GetAllByTypeID(3)
        JPT.Debugger(JPT.GetCenterOfEntities(listParts))
        ```
        
        """
        message = "JPT.GetCenterOfEntities({})".format(DItemVector)
        return JPT_RUN_LINE(message)

    def GetContactType(contactID):
        r"""
        ## Description
        
        Get Abaqus contact type after inputting contact ID.
        
        ## Syntax
        
        ```psj
        JPT.GetContactType(contactID)
        ```
        
        ## Inputs
        
        ### `contactID`
        
        - An _Integer_ specifying Abaqus contact ID.
        - This is a required input.
        
        ## Return Code
        
        - **-1**: Inputted _contactID_ does not exist on the model.
        - **0**: Inputted _contactID_ is a _General_ contact type.
        - **1**: Inputted _contactID_ is a _Tied_ contact type.
        - **2**: Inputted _contactID_ is a _All with self_ contact type.
        
        ## Sample Code
        
        ```psj {3}
        # Make a function to return detail description of contact type
        def contact_case(iContactID: int) -> int:
            iContactType = JPT.GetContactType(iContactID)
            switch = {-1: "Error - Inputted contact ID {} does not exist on the model".format(iContactID),
                      0: "Inputted contact ID {} - Type = General Contact".format(iContactID),
                      1: "Inputted contact ID {} - Type = Tied Contact".format(iContactID),
                      2: "Inputted contact ID {} - Type = All with self Contact".format(iContactID)}
            return switch.get(iContactType)
        
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
        Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
        Tools.Group.CreateGroup(strGroupName="ContactAbaqus_2_Manual_Face_M", crlTargets=[Face(49)])
        Tools.Group.CreateGroup(strGroupName="ContactAbaqus_2_Manual_Face_S", crlTargets=[Face(76)])
        Connections.Contacts.Abaqus.ManualFace(strName="ContactAbaqus_2", dAdjustWidth=DFLT_DBL, dExtensionZone=DFLT_DBL,
            dMaxPenetration=DFLT_DBL, dSmoothAngle=DFLT_DBL, iFrictionType=-1, dFrictionCoeff1=DFLT_DBL,
            dFrictionCoeff2=DFLT_DBL, dShearStressLimit=DFLT_DBL, dSlipTolerance=DFLT_DBL, dStaticFrictionCoeff=DFLT_DBL,
            dKineticFrictionCoeff=DFLT_DBL, dDecayCoeff=DFLT_DBL, bAdjustPosition=True, dPositionTolerance=DFLT_DBL,
            iFormulationType=-1, iPressureOverclosureType=-1, dContactStiffness=DFLT_DBL, tshPressureOverclosure=[0, 0],
            iThermalConductanceDef=-1, tshClearanceData=[1, 2, DFLT_DBL, DFLT_DBL],
            tshPressureData=[1, 2, DFLT_DBL, DFLT_DBL], crplTargets=[CursorPair(Group(1), Group(2))],
            iContactColor=16711680)
        Tools.Group.CreateGroup(strGroupName="ContactAbaqus_3_Manual_Face_M", crlTargets=[Face(24)])
        Tools.Group.CreateGroup(strGroupName="ContactAbaqus_3_Manual_Face_S", crlTargets=[Face(75)])
        Connections.Contacts.Abaqus.ManualFace(strName="ContactAbaqus_3", iContactType=1, dAdjustWidth=DFLT_DBL,
            dExtensionZone=DFLT_DBL, dMaxPenetration=DFLT_DBL, dSmoothAngle=DFLT_DBL, iFrictionType=-1,
            dFrictionCoeff1=DFLT_DBL, dFrictionCoeff2=DFLT_DBL, dShearStressLimit=DFLT_DBL, dSlipTolerance=DFLT_DBL,
            dStaticFrictionCoeff=DFLT_DBL, dKineticFrictionCoeff=DFLT_DBL, dDecayCoeff=DFLT_DBL, bAdjustPosition=True,
            dPositionTolerance=DFLT_DBL, iFormulationType=-1, iPressureOverclosureType=-1, dContactStiffness=DFLT_DBL,
            tshPressureOverclosure=[0, 0], iThermalConductanceDef=-1, tshClearanceData=[1, 2, DFLT_DBL, DFLT_DBL],
            tshPressureData=[1, 2, DFLT_DBL, DFLT_DBL], crplTargets=[CursorPair(Group(3), Group(4))],
            iContactColor=16711680)
        
        # Output of the JPT.GetContactType utilities
        JPT.Debugger(contact_case(2))
        ```
        
        """
        message = "JPT.GetContactType({})".format(contactID)
        return JPT_RUN_LINE(message)

    def GetCountByType(DItemType):
        r"""
        ## Description
        
        Get total number of entities by inputting _[DItemType](../data-type/psj-command/DItem-types)_.
        
        ## Syntax
        
        ```psj
        JPT.GetCountByType(DItemType)
        ```
        
        ## Inputs
        
        ### `DItemType`
        
        - An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ that wants to count the total number.
        - This is a required input.
        
        ## Return Code
        
        An _Integer_ specifying the total number of the inputted type.
        
        ## Sample Code
        
        ```psj {9}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Count the total number of bodies existing on the current Jupiter
        iPartCount = JPT.GetCountByType(JPT.DItemType.BODY)
        print(iPartCount) # 3
        ```
        
        """
        message = "JPT.GetCountByType({})".format(DItemType)
        return JPT_RUN_LINE(message)

    def GetCurrentAnimation():
        r"""
        ## Description
        
        Get all current settings of Animation.
        
        ## Syntax
        
        ```psj
        JPT.GetCurrentAnimation()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _Dictionary_ specifying all current settings of Animation.
        
        ## Sample Code
        
        ```psj {2}
        # Get all currently settings of Animation
        animationDict = JPT.GetCurrentAnimation()
        
        # Dump out result
        pprint(animationDict)
        
        # Print out the Frame number
        print("Frame Number: " + str(animationDict["FrameNumber"]))
        ```
        
        """
        message = "JPT.GetCurrentAnimation({})".format('')
        return JPT_RUN_LINE(message)

    def GetCurrentCircle():
        r"""
        ## Description
        
        Get all current settings of Circle.
        
        ## Syntax
        
        ```psj
        JPT.GetCurrentCircle()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _Dictionary_ specifying all settings of the currently displaying Circle.
        
        ## Sample Code
        
        ```psj {2}
        # Get all currently settings of Circle
        circleDict = JPT.GetCurrentCircle()
        
        # Dump out result
        pprint(circleDict)
        
        # Print out the Highlight color
        colorRGB = JPT.ConvertJPTColorToRGB(circleDict["HighlightColor"])
        print("Highlight Color: " + colorRGB)
        ```
        
        """
        message = "JPT.GetCurrentCircle({})".format('')
        return JPT_RUN_LINE(message)

    def GetCurrentContour():
        r"""
        ## Description
        
        Get all current settings of Contour.
        
        ## Syntax
        
        ```psj
        JPT.GetCurrentContour()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _Dictionary_ specifying all settings of the currently displaying Contour.
        
        ## Sample Code
        
        ```psj {2}
        # Get all currently settings of Contour
        contourDict = JPT.GetCurrentContour()
        
        # Dump out result
        pprint(contourDict)
        
        # Print out the Upper color
        colorRGB = JPT.ConvertJPTColorToRGB(contourDict["UpperColor"])
        print("Upper Color: " + colorRGB)
        ```
        
        """
        message = "JPT.GetCurrentContour({})".format('')
        return JPT_RUN_LINE(message)

    def GetCurrentCrossSection():
        r"""
        ## Description
        
        Get all current settings of Cross Section.
        
        ## Syntax
        
        ```psj
        JPT.GetCurrentCrossSection()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _Dictionary_ specifying all settings of the currently displaying Cross Section.
        
        ## Sample Code
        
        ```psj {2}
        # Get all currently settings of Cross Section
        crossDict = JPT.GetCurrentCrossSection()
        
        # Dump out result
        pprint(crossDict)
        
        # Print out the current position
        print("Current Position: " + str(crossDict["CurrentPosition"]))
        ```
        
        """
        message = "JPT.GetCurrentCrossSection({})".format('')
        return JPT_RUN_LINE(message)

    def GetCurrentDeformation():
        r"""
        ## Description
        
        Get all current settings of Deformation.
        
        ## Syntax
        
        ```psj
        JPT.GetCurrentDeformation()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _Dictionary_ specifying all settings of the currently displaying Deformation.
        
        ## Sample Code
        
        ```psj {2}
        # Get all currently settings of Deformation
        deformDict = JPT.GetCurrentDeformation()
        
        # Dump out result
        pprint(deformDict)
        
        # Print out the Edge color
        colorRGB = JPT.ConvertJPTColorToRGB(deformDict["EdgeColor"])
        print("Edge Color: " + colorRGB)
        ```
        
        """
        message = "JPT.GetCurrentDeformation({})".format('')
        return JPT_RUN_LINE(message)

    def GetCurrentDiagram():
        r"""
        ## Description
        
        Get all current settings of Diagram.
        
        ## Syntax
        
        ```psj
        JPT.GetCurrentDiagram()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _Dictionary_ specifying all settings of the currently displaying Diagram.
        
        ## Sample Code
        
        ```psj {2}
        # Get all currently settings of Diagram
        diagramDict = JPT.GetCurrentDiagram()
        
        # Dump out result
        pprint(diagramDict)
        
        # Print out the Positive color
        colorRGB = JPT.ConvertJPTColorToRGB(diagramDict["PositiveColor"])
        print("Positive Color: " + colorRGB)
        ```
        
        """
        message = "JPT.GetCurrentDiagram({})".format('')
        return JPT_RUN_LINE(message)

    def GetCurrentDocumentPath():
        r"""
        ## Description
        
        Get the path of the current working Jupiter file.
        
        ## Syntax
        
        ```psj
        JPT.GetCurrentDocumentPath()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _String_ specifying the full path to the current Jupiter file.
        
        ## Sample Code
        
        ```psj {2}
        # Open an existing Jupiter file (*.jtdb) or (*.jth5) before running the below code
        path = JPT.GetCurrentDocumentPath()
        print(path)
        ```
        
        """
        message = "JPT.GetCurrentDocumentPath({})".format('')
        return JPT_RUN_LINE(message)

    def GetCurrentVector():
        r"""
        ## Description
        
        Get all current settings of Vector.
        
        ## Syntax
        
        ```psj
        JPT.GetCurrentVector()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _Dictionary_ specifying all settings of the currently displaying Vector.
        
        ## Sample Code
        
        ```psj {2}
        # Get all currently settings of Vector
        vectorDict = JPT.GetCurrentVector()
        
        # Dump out result
        pprint(vectorDict)
        
        # Print out the Positive color
        colorRGB = JPT.ConvertJPTColorToRGB(vectorDict["PositiveColor"])
        print("Positive Color: " + colorRGB)
        ```
        
        """
        message = "JPT.GetCurrentVector({})".format('')
        return JPT_RUN_LINE(message)

    def GetCurrentViewPoint():
        r"""
        ## Description
        
        Get all current settings of ViewPoint.
        
        ## Syntax
        
        ```psj
        JPT.GetCurrentViewPoint()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _Dictionary_ specifying all settings of the currently displaying ViewPoint.
        
        ## Sample Code
        
        ```psj {2}
        # Get all currently settings of ViewPoint
        viewDict = JPT.GetCurrentViewPoint()
        
        # Dump out result
        pprint(viewDict)
        
        # Print out the Scale factor
        print("Scale Factor: " + str(viewDict["ScaleFactor"]))
        ```
        
        """
        message = "JPT.GetCurrentViewPoint({})".format('')
        return JPT_RUN_LINE(message)

    def GetDefaultResultOption(PostAnalysisType, resultSet, timeStep, resultName, componentName, PostResultDataLoc):
        r"""
        ## Description
        
        Get default result option setting of the inputted result type.
        
        ## Syntax
        
        ```psj
        JPT.GetDefaultResultOption(PostAnalysisType,
                                   resultSet,
                                   timeStep,
                                   resultName,
                                   componentName,
                                   PostResultDataLoc)
        ```
        
        ## Inputs
        
        ### `PostAnalysisType`
        
        - An _Enum_ specifying the _[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.
        - This is a required input.
        
        ### `resultSet`
        
        - An _Integer_ specifying the step ID of the imported result.
        - This is a required input.
        
        ### `timeStep`
        
        - An _Integer_ specifying the time step of the imported result.
        - This is a required input.
        
        ### `resultName`
        
        - A _String_ specifying the type of result (Such as Displacement, Stress, etc.).
        - This is a required input.
        
        ### `componentName`
        
        - A _String_ specifying a specific direction of the result (Such as X, Y, Z, etc.).
        - This is a required input.
        
        ### `PostResultDataLoc`
        
        - An _Enum_ specifying the _[PostResultDataLoc](../data-type/psj-utility/post-utility/enumeration-types/post-result-data-loc-types)_ describing the location of result (Such as on node, on element, etc.).
        - This is a required input.
        
        ## Return Code
        
        A _[PostDataOp](../data-type/psj-utility/post-utility/post-built-in-types/post-data-op)_ object containing the default setting of the working result.
        
        ## Sample Code
        
        ```psj {5-12}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        default_result_option = \
            JPT.GetDefaultResultOption(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,
                                       1,
                                       1,
                                       "Displacement",
                                       "X",
                                       1)
        
        JPT.Debugger(default_result_option)
        
        # Component of PostDataOp
        print("Location: " + str(default_result_option.loc))
        print("Conversion: " + str(default_result_option.cnv))
        print("Continuously: " + str(default_result_option.cont))
        print("Coordinate: " + str(default_result_option.coord))
        print("Load 1D: " + str(default_result_option.load1d))
        print("Load 2D: " + str(default_result_option.load2d))
        print("Complex: " + str(default_result_option.complex))
        print("Phase Angle: " + str(default_result_option.phaseAngle))
        print("User Coordinate ID: " + str(default_result_option.userCoordSysId))
        ```
        
        <!-- [//]: # "amt is not used in the current version"
        
        <!-- print("Amplitude: " + str(default_result_option.amt)) -->
        
        """
        message = "JPT.GetDefaultResultOption({},{},{},{},{},{})".format(PostAnalysisType,resultSet,timeStep,resultName,componentName,PostResultDataLoc)
        return JPT_RUN_LINE(message)

    def GetDictMatPropKeys(dictMatProps):
        r"""
        ## Description
        
        Get list keys from dictMatProps.
        
        ## Syntax
        
        ```psj
        JPT.GetDictMatPropKeys(dictMatProps)
        ```
        
        ## Inputs
        
        ### `dictMatProps`
        
        - A _Dictionary_ specifying the _[dictMatProps](../data-type/psj-utility/pre-utility/built-in-types/DMaterial)_.
        - This is a required input.
        
        ## Return Code
        
        A _List of String_ specifying the keys of dictMatProps.
        
        ## Sample Code
        
        ```psj {11}
        # Get 1st material in the library materials
        mat0 = JPT.GetAllLibraryMaterials()[0]
        
        # Get & print dicMatProps
        dict1 = mat0.dictMatProps
        pprint(dict1)
        ```
        
        """
        message = "JPT.GetDictMatPropKeys({})".format(dictMatProps)
        return JPT_RUN_LINE(message)

    def GetDocumentByID(docID):
        r"""
        ## Description
        
        Get information of an indicated document by using its ID.
        
        ## Syntax
        
        ```psj
        JPT.GetDocumentByID(docID)
        ```
        
        ## Inputs
        
        ### `docID`
        
        - A _String_ specifying the ID of document to get information.
        - This is a required input.
        
        ## Return Code
        
        A _[Document](../data-type/psj-utility/pre-utility/built-in-types/Document)_ object specifying the information of document.
        
        ## Sample Code
        
        ```psj {2}
        doc = JPT.CreateNewDocument()
        docInfor = JPT.GetDocumentByID(doc.docID)
        JPT.Debugger(docInfor)
        ```
        
        """
        message = "JPT.GetDocumentByID({})".format(docID)
        return JPT_RUN_LINE(message)

    def GetDocumentByName(docName):
        r"""
        ## Description
        
        Get information of an indicated document by using its name.
        
        ## Syntax
        
        ```psj
        JPT.GetDocumentByName(docName)
        ```
        
        ## Inputs
        
        ### `docName`
        
        - A _String_ specifying the name of document to get information.
        - This is a required input.
        
        ## Return Code
        
        A _[Document](../data-type/psj-utility/pre-utility/built-in-types/Document)_ object specifying the information of document.
        
        ## Sample Code
        
        ```psj {3}
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
        docInfor = JPT.GetDocumentByName("101_solid")
        JPT.Debugger(docInfor)
        ```
        
        """
        message = "JPT.GetDocumentByName({})".format(docName)
        return JPT_RUN_LINE(message)

    def GetDocumentList():
        r"""
        ## Description
        
        Get information of all displaying documents.
        
        ## Syntax
        
        ```psj
        JPT.GetDocumentList()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _List of [Document](../data-type/psj-utility/pre-utility/built-in-types/Document)_ object specifying the information of all displaying documents.
        
        ## Sample Code
        
        ```psj {6}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        Home.ImportResults.Nastran(strPath=samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
        JPT.CreateNewDocument()
        # Get information of all displaying documents
        docList = JPT.GetDocumentList()
        for doc in docList:
            JPT.Debugger(doc)
        ```
        
        """
        message = "JPT.GetDocumentList({})".format('')
        return JPT_RUN_LINE(message)

    def GetElementResult(PostDataRangeType, resultValue, adjustment=1E-5):
        r"""
        ## Description
        
        Get elements with loaded results satisfy a condition.
        
        ## Syntax
        
        ```psj
        JPT.GetElementResult(PostDataRangeType,
                             resultValue,
                             adjustment)
        ```
        
        ## Inputs
        
        ### `PostDataRangeType`
        
        - An _Enum_ specifying the _[PostDataRangeType](../data-type/psj-utility/post-utility/enumeration-types/post-data-range-types)_ describing the condition to get the element results.
        - This is a required input.
        
        ### `resultValue`
        
        - A _Double_ specifying the referenced value.
        - This is a required input.
        
        ### `adjustment`
        
        - A _Double_ specifying the adjustment to the referenced value _[resultValue](#resultvalue)_:
          - If _[PostDataRangeType](../data-type/psj-utility/post-utility/enumeration-types/post-data-range-types)_ is a scalar type (i.e. EQ, NE, LT, GT, LE, GE), then the range to get the result is from (resultValue - adjustment) to (resultValue + adjustment)
          - If _[PostDataRangeType](../data-type/psj-utility/post-utility/enumeration-types/post-data-range-types)_ is a range type (i.e. IR, OR, IRE, ORE), then the range to get the result is from (resultValue) to (adjustment)
        - The default value is 1E-5.
        
        ## Return Code
        
        A _List of Cursor_ containing elements with loaded element results satisfy the given condition.
        
        ## Sample Code
        
        ```psj {11,15}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, Max Principal Stress, 2}, {2, 1, 0, 0, 0, 0, \
                                     0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, \
                                     0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, \
                                     0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')
        
        # Create a elemental group whose element results greater than 1 (tolerance=10E-3)
        list_element_1= JPT.GetElementResult(JPT.PostDataRangeType.GT,1,10E-3)
        Tools.Group.CreateGroup(strGroupName="Group_Element_1", crlTargets=list_element_1)
        
        # Create a elemental group whose element results in range (1,5)
        list_element_2= JPT.GetElementResult(JPT.PostDataRangeType.IR,1,5)
        Tools.Group.CreateGroup(strGroupName="Group_Element_2", crlTargets=list_element_2)
        ```
        
        """
        message = "JPT.GetElementResult({},{},{})".format(PostDataRangeType,resultValue,adjustment)
        return JPT_RUN_LINE(message)

    def GetElemsByKind(ElemKind):
        r"""
        ## Description
        
        Get a _List of Elements_ by inputting their kind (1D, 2D, 3D, etc.).
        
        ## Syntax
        
        ```psj
        JPT.GetElemsByKind(ElemKind)
        ```
        
        ## Inputs
        
        ### `ElemKind`
        
        - An _Enum_ specifying the _[ElemKind](../data-type/psj-command/element-types)_ of elements in Jupiter.
        - This is a required input.
        
        ## Return Code
        
        An _[ElemVector](../data-type/psj-utility/pre-utility/built-in-types/ElemVector)_ object or _List of [DElem](../data-type/psj-utility/pre-utility/built-in-types/DElem)_ objects containing all the information of the related elements having the element kind is the same as the inputted element kind.
        
        ## Sample Code
        
        ```psj {8}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Get the information of all existing 2D elements
        list2DElems = JPT.GetElemsByKind(JPT.ElemKind.ELEMKIND_2D)
        JPT.Debugger(list2DElems)
        
        # Print all the related information of each existing 2D element in list
        for elem in list2DElems:
            JPT.Debugger(elem)
        ```
        
        """
        message = "JPT.GetElemsByKind({})".format(ElemKind)
        return JPT_RUN_LINE(message)

    def GetElemsByType(ElemType):
        r"""
        ## Description
        
        Get a _List of Elements_ by inputting their type (Tri3, Hex8, Tet10, etc.).
        
        ## Syntax
        
        ```psj
        JPT.GetElemsByType(ElemType)
        ```
        
        ## Inputs
        
        ### `ElemType`
        
        - An _Enum_ specifying the _[ElemType](../data-type/psj-command/element-types)_ of elements in Jupiter.
        - This is a required input.
        
        ## Return Code
        
        An _[ElemVector](../data-type/psj-utility/pre-utility/built-in-types/ElemVector)_ object or _List of [DElem](../data-type/psj-utility/pre-utility/built-in-types/DElem)_ objects containing all the information of the related elements having the element type is the same as the inputted element type.
        
        ## Sample Code
        
        ```psj {77-84}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                           strName="Cube_2",
                           iPartColor=6409934)
        Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0],
                           strName="Cube_3",
                           iPartColor=13259210)
        Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0],
                           strName="Cube_4",
                           iPartColor=7697908)
        Geometry.Part.Cube(dlOrigin=[0.04, 0.0, 0.0],
                           strName="Cube_5",
                           iPartColor=7463537)
        Geometry.Part.Cube(dlOrigin=[0.05, 0.0, 0.0],
                           strName="Cube_6",
                           iPartColor=7434735)
        Geometry.Part.Cube(dlOrigin=[0.06, 0.0, 0.0],
                           strName="Cube_7",
                           iPartColor=14903267)
        Geometry.Part.Cube(dlOrigin=[0.07, 0.0, 0.0],
                           strName="Cube_8",
                           iPartColor=15658599)
        
        Meshing.SetMeshAttribute(crlParts=[Part(5, 6, 7, 8)],
                                 surfaceMesh=SURFACE_MESH(dGeomAngle=0.7853981634,
                                                          iPerformanceMode=1,
                                                          dAutoMergeTinyFacesAngle=0.5235987756,
                                                          bOutputQuadMesh=True,
                                                          bGeomApprox=True,
                                                          iNextEntityOffsetId=0))
        Meshing.SurfaceMeshing(crlParts=[Part(5, 6, 7, 8)],
                               surfaceMesh=SURFACE_MESH(dGeomAngle=0.7853981634,
                                                        iPerformanceMode=1,
                                                        dAutoMergeTinyFacesAngle=0.5235987756,
                                                        bOutputQuadMesh=True,
                                                        bGeomApprox=True,
                                                        iNextEntityOffsetId=0),
                                                        iThreadNum=12)
        MeshEdit.SurfaceMesh(crlParts=[Part(2, 4, 8, 6)])
        Meshing.SolidMeshing(crlParts=[Part(8, 4, 7, 3)],
                             dGradingFactor=1.05,
                             dStretchLimit=0.1,
                             iSpeedVsQual=1,
                             iRegion=1,
                             bSafeMode=False,
                             iParallel=12,
                             bInternalMeshOnly=False,
                             iPartColor=65280)
        Meshing.SolidMeshing(crlParts=[Part(4)],
                             bTet10=True,
                             dGradingFactor=1.05,
                             dStretchLimit=0.1,
                             iSpeedVsQual=1,
                             iRegion=1,
                             bSafeMode=False,
                             iParallel=12,
                             bInternalMeshOnly=False,
                             iPartColor=65280)
        
        del_faces = [208, 182, 178, 204, 206, 177, 203, 179, 205, 180]
        extrude_faces = [207, 181]
        
        Geometry.DeleteEntity.Face(crlFaces=[Face(*del_faces)])
        
        HexModeling.Linear(crlFaces=[Face(*extrude_faces)],
                           dLength=0.01,
                           iLayer=2,
                           vecSweepDirection=[0.0,
                                              0.0,
                                              1.0],
                           iLinearMethod=4)
        
        MeshEdit.SolidMesh(crlParts=[Part(8)])
        JPT.ViewFitToModel()
        
        listTri3Elems = JPT.GetElemsByType(JPT.ElemType.ELEMTYPE_TRI3)
        listTri6Elems = JPT.GetElemsByType(JPT.ElemType.ELEMTYPE_TRI6)
        listTet4Elems = JPT.GetElemsByType(JPT.ElemType.ELEMTYPE_TET4)
        listTet10Elems = JPT.GetElemsByType(JPT.ElemType.ELEMTYPE_TET10)
        listQuad4Elems = JPT.GetElemsByType(JPT.ElemType.ELEMTYPE_QUAD4)
        listQuad8Elems = JPT.GetElemsByType(JPT.ElemType.ELEMTYPE_QUAD8)
        listHex8Elems = JPT.GetElemsByType(JPT.ElemType.ELEMTYPE_HEX8)
        listHex20Elems = JPT.GetElemsByType(JPT.ElemType.ELEMTYPE_HEX20)
        
        JPT.Debugger(listTri3Elems)
        JPT.Debugger(listTri6Elems)
        JPT.Debugger(listTet4Elems)
        JPT.Debugger(listTet10Elems)
        JPT.Debugger(listQuad4Elems)
        JPT.Debugger(listQuad8Elems)
        JPT.Debugger(listHex8Elems)
        JPT.Debugger(listHex20Elems)
        ```
        
        """
        message = "JPT.GetElemsByType({})".format(ElemType)
        return JPT_RUN_LINE(message)

    def GetEntitiesByAdjacent(DItemType, entityID, angleValue):
        r"""
        ## Description
        
        Get _List of Objects_ by adjacency based on the stop angle.
        
        ## Syntax
        
        ```psj
        JPT.GetEntitiesByAdjacent(DItemType, entityID, angleValue)
        ```
        
        ## Inputs
        
        ### `DItemType`
        
        - An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.
        - This is a required input.
        
        ### `entityID`
        
        - An _Integer_ specifying the ID of the starting entity.
        - This is a required input.
        
        ### `angleValue`
        
        - An _Integer_ specifying the stop angle between entities for searching.
        - This is a required input.
        
        ## Return Code
        
        A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing all the information of found entities.
        
        ## Sample Code
        
        ```psj {6}
        # Prepare model
        Geometry.Part.Cube()
        JPT.ViewFitToModel()
        
        # Get the faces relating to the face with ID = 26 based on angle = 30
        adjacentFaces = JPT.GetEntitiesByAdjacent(JPT.DItemType.FACE, 26, 30)
        JPT.Debugger(adjacentFaces)
        ```
        
        """
        message = "JPT.GetEntitiesByAdjacent({},{},{})".format(DItemType,entityID,angleValue)
        return JPT_RUN_LINE(message)

    def GetEntitiesByAssociation(DItemType, AssociateType, entityID):
        r"""
        ## Description
        
        Get _List of Objects_ by associating from the inputted entity ID and its type.
        
        ## Syntax
        
        ```psj
        JPT.GetEntitiesByAssociation(DItemType, AssociateType, entityID)
        ```
        
        ## Inputs
        
        ### `DItemType`
        
        - An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.
        - This is a required input.
        
        ### `AssociateType`
        
        - An _Enum_ specifying the _[AssociateType](../data-type/psj-utility/pre-utility/enumeration-types/associate-types)_ describing the association type in Jupiter.
        - This is a required input.
        
        ### `entityID`
        
        - An _Integer_ specifying the ID of which is used as a starting entity.
        - This is a required input.
        
        ## Return Code
        
        A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing all the information of associated entities.
        
        ## Sample Code
        
        ```psj {6}
        # Prepare model
        Geometry.Part.Cube()
        JPT.ViewFitToModel()
        
        # Get all the associating faces existing on the part with ID = 1
        listAssociatedEntities = JPT.GetEntitiesByAssociation(JPT.DItemType.BODY, JPT.AssociateType.AS_FACE, 1)
        JPT.Debugger(listAssociatedEntities) # return value is a list DItem has size = 6
        ```
        
        """
        message = "JPT.GetEntitiesByAssociation({},{},{})".format(DItemType,AssociateType,entityID)
        return JPT_RUN_LINE(message)

    def GetEntitiesByID(DItemType, itemID):
        r"""
        ## Description
        
        Get information of the inputted entity ID.
        
        ## Syntax
        
        ```psj
        JPT.GetEntitiesByID(DItemType, itemID)
        ```
        
        ## Inputs
        
        ### `DItemType`
        
        - An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.
        - This is a required input.
        
        ### `itemID`
        
        - An _Integer_ specifying the ID of the target entity.
        - This is a required input.
        
        ## Return Code
        
        A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing the information of the entity has the inputted ID.
        
        Note that the inputted entity is the first element of this list.
        
        ## Sample Code
        
        ```psj {8}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Get the information of the part with ID = 2 and store it to a list
        listParts = JPT.GetEntitiesByID(JPT.DItemType.BODY, 2)
        
        # Print the information of the part
        JPT.Debugger(listParts[0])
        ```
        
        """
        message = "JPT.GetEntitiesByID({},{})".format(DItemType,itemID)
        return JPT_RUN_LINE(message)

    def GetEntitiesByName(DTableType, itemName, BoolType):
        r"""
        ## Description
        
        Get information of the inputted entity name.
        
        ## Syntax
        
        ```psj
        JPT.GetEntitiesByName(DTableType, itemName, BoolType)
        ```
        
        ## Inputs
        
        ### `DTableType`
        
        - An _Enum_ specifying the _[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_ of entity in Jupiter.
        - This is a required input.
        
        ### `itemName`
        
        - A _String_ specifying the name of the target entity.
        - This is a required input.
        
        ### `BoolType`
        
        - An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the matching type:
          - _False_: Approximate match.
          - _True_: Exact match.
        - This is a required input.
        
        ## Return Code
        
        A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing the information of the entities have the inputted name.
        
        ## Sample Code
        
        ```psj {8}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Get the information of the part with name = "_" and store it to a list
        listParts = JPT.GetEntitiesByName(JPT.DTableType.DTABLE_BODY, "_", JPT.BoolType.FALSE_VAL)
        print(listParts[0].name) # Cube_1
        print(listParts[2].name) # Cube_3
        print(listParts[2].id) # 3
        ```
        
        """
        message = "JPT.GetEntitiesByName({},{},{})".format(DTableType,itemName,BoolType)
        return JPT_RUN_LINE(message)

    def GetEntitiesByPosition(AssociateType, xCoordValue, yCoordValue, zCoordValue):
        r"""
        ## Description
        
        Get the entity satisfying the given conditions (X, Y, Z).
        
        ## Syntax
        
        ```psj
        JPT.GetEntitiesByPosition(AssociateType, xCoordValue, yCoordValue, zCoordValue)
        ```
        
        ## Inputs
        
        ### `AssociateType`
        
        - An _Enum_ specifying the _[AssociateType](../data-type/psj-utility/pre-utility/enumeration-types/associate-types)_ describing the association type in Jupiter.
        - This is a required input.
        
        ### `xCoordValue`
        
        - A _Double_ specifying the value in X coordinate in millimeters [mm] in the Cartesian coordinate system..
        - This is a required input.
        
        ### `yCoordValue`
        
        - A _Double_ specifying the value in Y coordinate in millimeters [mm] in the Cartesian coordinate system..
        - This is a required input.
        
        ### `zCoordValue`
        
        - A _Double_ specifying the value in Z coordinate in millimeters [mm] in the Cartesian coordinate system..
        - This is a required input.
        
        ## Return Code
        
        A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing the information of the satisfied entity.
        
        Note that to get the satisfied entity, please get the second element of the created _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_.
        
        ## Sample Code
        
        ```psj {6}
        # Prepare model
        Geometry.Part.Cube()
        JPT.ViewFitToModel()
        
        # Get the information of the created cube
        selPart = JPT.GetEntitiesByPosition(JPT.AssociateType.AS_BODY, 10, 10, 10)
        JPT.Debugger(selPart[0]) # second element of the created list
        ```
        
        """
        message = "JPT.GetEntitiesByPosition({},{},{},{})".format(AssociateType,xCoordValue,yCoordValue,zCoordValue)
        return JPT_RUN_LINE(message)

    def GetGroupFromSubGroup(groupName):
        r"""
        ## Description
        
        Get the _List of Groups_ under the specified group's name.
        
        ## Syntax
        
        ```psj
        JPT.GetGroupFromSubGroup(groupName)
        ```
        
        ## Inputs
        
        ### `groupName`
        
        - A _String_ specifying the name of the existing group using for getting all the information of the group inside.
        - This is a required input.
        
        ## Return Code
        
        A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects specifying groups which are under the specified group's name.
        
        ## Sample Code
        
        ```psj {242,245}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                           strName="Cube_2",
                           iPartColor=6409934)
        Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0],
                           strName="Cube_3",
                           iPartColor=13259210)
        Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0],
                           strName="Cube_4",
                           iPartColor=7697908)
        Geometry.Part.Cube(dlOrigin=[0.04, 0.0, 0.0],
                           strName="Cube_5",
                           iPartColor=7463537)
        Geometry.Part.Cube(dlOrigin=[0.05, 0.0, 0.0],
                           strName="Cube_6",
                           iPartColor=7434735)
        Geometry.Part.Cube(dlOrigin=[0.06, 0.0, 0.0],
                           strName="Cube_7",
                           iPartColor=14903267)
        Geometry.Part.Cube(dlOrigin=[0.07, 0.0, 0.0],
                           strName="Cube_8",
                           iPartColor=15658599)
        JPT.ViewFitToModel()
        
        Meshing.SetMeshAttribute(crlParts=[Part(5, 6, 7, 8)],
                                 surfaceMesh=SURFACE_MESH(dGeomAngle=0.7853981634,
                                                          iPerformanceMode=1,
                                                          dAutoMergeTinyFacesAngle=0.5235987756,
                                                          bOutputQuadMesh=True,
                                                          bGeomApprox=True,
                                                          iNextEntityOffsetId=0))
        Meshing.SurfaceMeshing(crlParts=[Part(5, 6, 7, 8)],
                               surfaceMesh=SURFACE_MESH(dGeomAngle=0.7853981634,
                                                        iPerformanceMode=1,
                                                        dAutoMergeTinyFacesAngle=0.5235987756,
                                                        bOutputQuadMesh=True,
                                                        bGeomApprox=True,
                                                        iNextEntityOffsetId=0),
                                                        iThreadNum=12)
        MeshEdit.SurfaceMesh(crlParts=[Part(2, 4, 8, 6)])
        Meshing.SolidMeshing(crlParts=[Part(8, 4, 7, 3)],
                             dGradingFactor=1.05,
                             dStretchLimit=0.1,
                             iSpeedVsQual=1,
                             iRegion=1,
                             bSafeMode=False,
                             iParallel=12,
                             bInternalMeshOnly=False,
                             iPartColor=65280)
        Meshing.SolidMeshing(crlParts=[Part(4)],
                             bTet10=True,
                             dGradingFactor=1.05,
                             dStretchLimit=0.1,
                             iSpeedVsQual=1,
                             iRegion=1,
                             bSafeMode=False,
                             iParallel=12,
                             bInternalMeshOnly=False,
                             iPartColor=65280)
        
        del_faces = [208, 182, 178, 204, 206, 177, 203, 179, 205, 180]
        extrude_faces = [207, 181]
        
        Geometry.DeleteEntity.Face(crlFaces=[Face(*del_faces)])
        
        HexModeling.Linear(crlFaces=[Face(*extrude_faces)],
                           dLength=0.01,
                           iLayer=2,
                           vecSweepDirection=[0.0,
                                              0.0,
                                              1.0],
                           iLinearMethod=4)
        
        MeshEdit.SolidMesh(crlParts=[Part(8)])
        
        Properties.Material.Add(strMaterialName="Copper_Alloy",
                                listMaterialProperty=[Density([(DENSITY,
                                                                8.3e-09)]),
                                                      Elastic([(YOUNGS_MODULUS,
                                                                110000.0),
                                                               (POISSONS_RATIO,
                                                                0.34)])])
        Properties.Material.Add(strMaterialName="Magnesium_Alloy",
                                listMaterialProperty=[Density([(DENSITY,
                                                                1.8e-09)]),
                                                      Elastic([(YOUNGS_MODULUS,
                                                                45000.0),
                                                               (POISSONS_RATIO,
                                                                0.35)])])
        Properties.Material.Add(strMaterialName="Concrete",
                                listMaterialProperty=[Density([(DENSITY,
                                                                2.3e-09)]),
                                                      Elastic([(YOUNGS_MODULUS,
                                                                30000.0),
                                                               (POISSONS_RATIO,
                                                                0.18)])])
        Properties.Material.Add(strMaterialName="Polyethylene",
                                listMaterialProperty=[Density([(DENSITY,
                                                                9.5e-10)]),
                                                      Elastic([(YOUNGS_MODULUS,
                                                                1100.0),
                                                               (POISSONS_RATIO,
                                                                0.42)])])
        Properties.Material.Add(strMaterialName="Structural_Steel",
                                listMaterialProperty=[Density([(DENSITY,
                                                                7.85e-09)]),
                                                      Elastic([(YOUNGS_MODULUS,
                                                                200000.0),
                                                               (POISSONS_RATIO,
                                                                0.3)])])
        Properties.Material.Add(strMaterialName="Stainless_Steel",
                                listMaterialProperty=[Density([(DENSITY,
                                                                7.75e-09)]),
                                                      Elastic([(YOUNGS_MODULUS,
                                                                193000.0),
                                                               (POISSONS_RATIO,
                                                                0.31)])])
        Properties.Material.Add(strMaterialName="Titanium_Alloy",
                                listMaterialProperty=[Density([(DENSITY,
                                                                4.62e-09)]),
                                                      Elastic([(YOUNGS_MODULUS,
                                                                96000.0),
                                                               (POISSONS_RATIO,
                                                                0.36)])])
        Properties.Material.Add(strMaterialName="Aluminum_Alloy",
                                listMaterialProperty=[Density([(DENSITY,
                                                                2.7699999999999997e-09)]),
                                                      Elastic([(YOUNGS_MODULUS,
                                                                71000.0),
                                                               (POISSONS_RATIO,
                                                                0.33)])])
        
        Properties.Solid(crlTargets=[Part(3)],
                         strName="Cube_3",
                         iPropertyColor=16131973,
                         crMaterial=Material(1),
                         iCordM=-2,
                         dDynaRemeshVal1=DFLT_DBL,
                         dDynaRemeshVal2=DFLT_DBL,
                         dDispHG=DFLT_DBL,
                         iFLG=-1)
        Properties.Solid(crlTargets=[Part(4)],
                         strName="Cube_4",
                         iPropertyId=2,
                         iPropertyColor=10176523,
                         crMaterial=Material(2),
                         iCordM=-2,
                         dDynaRemeshVal1=DFLT_DBL,
                         dDynaRemeshVal2=DFLT_DBL,
                         dDispHG=DFLT_DBL,
                         iFLG=-1)
        Properties.Solid(crlTargets=[Part(7)],
                         strName="Cube_7",
                         iPropertyId=3,
                         iPropertyColor=4185823,
                         crMaterial=Material(3),
                         iCordM=-2,
                         dDynaRemeshVal1=DFLT_DBL,
                         dDynaRemeshVal2=DFLT_DBL,
                         dDispHG=DFLT_DBL,
                         iFLG=-1)
        Properties.Solid(crlTargets=[Part(8)],
                         strName="Cube_8",
                         iPropertyId=4,
                         iPropertyColor=14470647,
                         crMaterial=Material(4),
                         iCordM=-2,
                         dDynaRemeshVal1=DFLT_DBL,
                         dDynaRemeshVal2=DFLT_DBL,
                         dDispHG=DFLT_DBL,
                         iFLG=-1)
        
        Properties.Shell(crlTargets=[Part(1)],
                         strName="Cube_1",
                         iPropertyId=5,
                         iPropertyColor=6438968,
                         crMatMembrane=Material(5),
                         crMatBend=Material(5),
                         crMatShear=Material(5),
                         dMatOrient1=DFLT_DBL,
                         dThickness=0.001,
                         dBendStiff=DFLT_DBL,
                         dThickRatio=DFLT_DBL,
                         dNSM=DFLT_DBL,
                         dFiberDist1=DFLT_DBL,
                         dFiberDist2=DFLT_DBL,
                         dPlateOff=DFLT_DBL,
                         iItgPts=DFLT_INT)
        Properties.Shell(crlTargets=[Part(2)],
                         strName="Cube_2",
                         iPropertyId=6,
                         iPropertyColor=12901905,
                         crMatMembrane=Material(6),
                         crMatBend=Material(6),
                         crMatShear=Material(6),
                         dMatOrient1=DFLT_DBL,
                         dThickness=0.001,
                         dBendStiff=DFLT_DBL,
                         dThickRatio=DFLT_DBL,
                         dNSM=DFLT_DBL,
                         dFiberDist1=DFLT_DBL,
                         dFiberDist2=DFLT_DBL,
                         dPlateOff=DFLT_DBL,
                         iItgPts=DFLT_INT)
        Properties.Shell(crlTargets=[Part(5)],
                         strName="Cube_5",
                         iPropertyId=7,
                         iPropertyColor=13102932,
                         crMatMembrane=Material(7),
                         crMatBend=Material(7),
                         crMatShear=Material(7),
                         dMatOrient1=DFLT_DBL,
                         dThickness=0.001,
                         dBendStiff=DFLT_DBL,
                         dThickRatio=DFLT_DBL,
                         dNSM=DFLT_DBL,
                         dFiberDist1=DFLT_DBL,
                         dFiberDist2=DFLT_DBL,
                         dPlateOff=DFLT_DBL,
                         iItgPts=DFLT_INT)
        Properties.Shell(crlTargets=[Part(6)],
                         strName="Cube_6",
                         iPropertyId=8,
                         iPropertyColor=652495,
                         crMatMembrane=Material(7),
                         crMatBend=Material(7),
                         crMatShear=Material(7),
                         dMatOrient1=DFLT_DBL,
                         dThickness=0.001,
                         dBendStiff=DFLT_DBL,
                         dThickRatio=DFLT_DBL,
                         dNSM=DFLT_DBL,
                         dFiberDist1=DFLT_DBL,
                         dFiberDist2=DFLT_DBL,
                         dPlateOff=DFLT_DBL,
                         iItgPts=DFLT_INT)
        
        Groups.RightClick.CreateMatGroup()
        Groups.RightClick.PropertyGroup()
        
        mat_group = JPT.GetGroupFromSubGroup("Material Group 1")
        JPT.Debugger(mat_group)
        
        prop_group = JPT.GetGroupFromSubGroup("Property Group 1")
        JPT.Debugger(prop_group)
        ```
        
        """
        message = "JPT.GetGroupFromSubGroup({})".format(groupName)
        return JPT_RUN_LINE(message)

    def GetInternalIDRefItem(DItemType, externalID, bUsedRef):
        r"""
        ## Description
        
        Get internal ID of a reference entity.
        
        ## Syntax
        
        ```psj
        JPT.GetInternalIDRefItem(...)
        ```
        
        ## Inputs
        
        ### `DItemType`
        - An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ describing the type of entity (reference entities here). 
        - This is a required input.
        
        ### `externalID`
        - An _Int_ specifying external ID of reference item.
        - This is a required input.
        
        ### `bUsedRef`
        - A _Bool_ specifying if the target is reference item.
        - The defalut value is True.
        
        ## Return Code
        
        A _Int_ value that indicates internal ID of the reference entity.
        
        ## Sample Code
        
        ```psj {37}
        Geometry.Part.Cube()
        
        Tools.Renumber(
            listRenumberItem=[
                RENUMBER_ITEM(crTarget=Part(1), 
                iBeginID=1000, 
                iTargetType=5,
                iCount=6, 
                ilOffset=[10000, 100, 1], 
            dlCoordTolerance=[0.1, 0.1, 0.1], 
            bEnable=True)])
        
        Meshing.AdjustCircleVertex(crlParts=[Part(1)], bInModeSurfaceMesh=True)
        
        Meshing.SetMeshAttribute(
            crlParts=[Part(1)], 
            surfaceMesh=SURFACE_MESH(
                dMaxElemSize=0.05, 
                dMinElemSize=0.0001, 
                dGeomAngle=0.7853981634,
                dGeomMinSize=0.0001, 
                iPerformanceMode=1, 
                dAutoMergeTinyFacesAngle=0.5235987756, bGeomApprox=True, iNextEntityOffsetId=0)
                 )
        
        Meshing.SurfaceMeshing(
            crlParts=[Part(1)], 
            surfaceMesh=SURFACE_MESH(
                dMaxElemSize=0.05, 
                dMinElemSize=0.0001, 
                dGeomAngle=0.7853981634, 
                dGeomMinSize=0.0001, 
                iPerformanceMode=1, 
                dAutoMergeTinyFacesAngle=0.5235987756, bGeomApprox=True, iNextEntityOffsetId=0)
                )
        
        result=JPT.GetInternalIDRefItem(JPT.DItemType.REF_FACE,1005)
        print(result)
        ```
        
        """
        message = "JPT.GetInternalIDRefItem({},{},{})".format(DItemType,externalID,bUsedRef)
        return JPT_RUN_LINE(message)

    def GetJPTTempPath():
        r"""
        ## Description
        
        Get the path to the temporary folder of the current Jupiter program.
        
        ## Syntax
        
        ```psj
        JPT.GetJPTTempPath()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _String_ specifying the path to the current Jupiter temporary folder.
        
        ## Sample Code
        
        ```psj {2}
        # Get the current Jupiter temporary folder
        path = JPT.GetJPTTempPath()
        JPT.Debugger(path)
        ```
        
        """
        message = "JPT.GetJPTTempPath({})".format('')
        return JPT_RUN_LINE(message)

    def GetJTDBVersion():
        r"""
        ## Description
        
        Get all the version information of the current Jupiter file.
        
        ## Syntax
        
        ```psj
        JPT.GetJTDBVersion()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[VersionInfo](../data-type/psj-utility/pre-utility/built-in-types/VersionInfo)_ object specifying a _List_ containing the version information of the current Jupiter file, including:
        
        - Build
        - Major
        - Minor
        - Sub
        
        ## Sample Code
        
        ```psj {2}
        # Get the version information of the current Jupiter
        version = JPT.GetJTDBVersion()
        JPT.Debugger(version)
        ```
        
        """
        message = "JPT.GetJTDBVersion({})".format('')
        return JPT_RUN_LINE(message)

    def GetLastCreatedCursor():
        r"""
        ## Description
        
        Get the information of the last created entity.
        
        ## Syntax
        
        ```psj
        JPT.GetLastCreatedCursor()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing the information of the last created object.
        
        ## Sample Code
        
        ```psj {8}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Get the information of the last created part
        lastCreatedCursor = JPT.GetLastCreatedCursor()
        JPT.Debugger(lastCreatedCursor[0]) # Cube_3
        ```
        
        """
        message = "JPT.GetLastCreatedCursor({})".format('')
        return JPT_RUN_LINE(message)

    def GetMacroLog():
        r"""
        ## Description
        
        Get the current text existing on the Macro window.
        
        ## Syntax
        
        ```psj
        JPT.GetMacroLog()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _String_ containing all the existing text on the Macro window.
        
        ## Sample Code
        
        ```psj {5}
        # Do some operations, such as open a dialog of a function or
        # creating something to store its macro to the Macro window
        # In case the Macro dialog is blanked, its returning value is ""
        # Get the stored macro on the Macro window
        storedMacro = JPT.GetMacroLog()
        JPT.Debugger(storedMacro)
        ```
        
        """
        message = "JPT.GetMacroLog({})".format('')
        return JPT_RUN_LINE(message)

    def GetMaterialDBById(userMaterialID):
        r"""
        ## Description
        
        Check whether the inputted material ID is existing in the user material database or not.
        
        ## Syntax
        
        ```psj
        JPT.GetMaterialDBById(userMaterialID)
        ```
        
        ## Inputs
        
        ### `userMaterialID`
        
        - An _Integer_ specifying the material ID wants to check in user material database.
        - This is a required input.
        
        ## Return Code
        
        An _Integer_ specifying the ID of the checked material if it exists in user material database.
        It will return the value as below:
        
        - **`0`**: if the checked material ID does not exist in user material database.
        - **`userMaterialID`**: return back the inputted ID if the checked material ID is existing in user material database.
        
        ## Sample Code
        
        ```psj {11,16}
        # Create user material data base
        Properties.Material.Add("Copper_Alloy", [Density([(DENSITY, 8.3e-09)]),
                                Elastic([(YOUNGS_MODULUS, 110000.0), (POISSONS_RATIO, 0.34)])])
                                # User material ID = 1 (Existing in the Library material database)
        
        # Check the ID of the created material whether it's existing in the
        # user material database or not
        
        # Return 1 - The checked material is existing in the user material database and
        # return the ID of its which is the same as inputted ID
        firstMat = JPT.GetMaterialDBById(1)
        JPT.Debugger(firstMat)
        
        # Return 0 - Does not exist in the user material database
        # with inputted material ID = 2
        secondMat = JPT.GetMaterialDBById(2)
        JPT.Debugger(secondMat)
        ```
        
        """
        message = "JPT.GetMaterialDBById({})".format(userMaterialID)
        return JPT_RUN_LINE(message)

    def GetMaterialFromProperty(propertyID):
        r"""
        ## Description
        
        Get the used material information (Name, ID, etc.) from the inputted property ID if it's exist.
        
        ## Syntax
        
        ```psj
        JPT.GetMaterialFromProperty(propertyID)
        ```
        
        ## Inputs
        
        ### `propertyID`
        
        - An _Integer_ specifying the material property ID.
        - This is a required input.
        
        ## Return Code
        
        A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object containing information of the material using for the inputted property.
        
        ## Sample Code
        
        ```psj {20,27}
        # Prepare model
        Geometry.Part.Cube(iPartColor=7731061)
        Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=11908427)
        JPT.ViewFitToModel()
        Meshing.SolidMeshing(crlParts=[Part(2)], bTet10=True, dGradingFactor=1.05, dStretchLimit=0.1, iSpeedVsQual=1,
            iRegion=1, bSafeMode=False, iParallel=4, bInternalMeshOnly=False, iPartColor=65280)
        Properties.Material.Add("Concrete", [Density([(DENSITY, 2.3e-09)]), Elastic([(YOUNGS_MODULUS, 30000.0),
            (POISSONS_RATIO, 0.18)])])
        Properties.Material.Add("Magnesium_Alloy", [Density([(DENSITY, 1.8e-09)]), Elastic([(YOUNGS_MODULUS, 45000.0),
            (POISSONS_RATIO, 0.35)])])
        Properties.Shell(crlTargets=[Face(26, 25)], strName="Shell Property 1", iPropertyColor=16131973,
            crMatMembrane=Material(1), crMatBend=Material(1), crMatShear=Material(1), dMatOrient1=DFLT_DBL,
            dThickness=0.001, dBendStiff=DFLT_DBL, dThickRatio=DFLT_DBL, dNSM=DFLT_DBL, dFiberDist1=DFLT_DBL,
            dFiberDist2=DFLT_DBL, dPlateOff=DFLT_DBL, iItgPts=DFLT_INT)
        Properties.Solid(crlTargets=[Part(2)], strName="Solid Property 2", iPropertyId=2, iPropertyColor=4955455,
            crMaterial=Material(2), iCordM=-2, dDynaRemeshVal1=DFLT_DBL, dDynaRemeshVal2=DFLT_DBL, dDispHG=DFLT_DBL,
            iFLG=-1)
        
        # Get material information of the property with ID = 1 (Shell)
        dItemShellMat = JPT.GetMaterialFromProperty(1)
        JPT.Debugger(dItemShellMat)
        print("Applied material on shells: ")
        print("--- Name: %s" %str(dItemShellMat.name))
        print("--- ID: %s" %str(dItemShellMat.id))
        
        # Get material information of the property with ID = 2 (Solid)
        dItemSolidlMat = JPT.GetMaterialFromProperty(2)
        JPT.Debugger(dItemSolidlMat)
        print("Applied material on solid: ")
        print("--- Name: %s" %str(dItemSolidlMat.name))
        print("--- ID: %s" %str(dItemSolidlMat.id))
        ```
        
        """
        message = "JPT.GetMaterialFromProperty({})".format(propertyID)
        return JPT_RUN_LINE(message)

    def GetMaterialXML():
        r"""
        ## Description
        
        Get the information of all user material in xml format.
        
        ## Syntax
        
        ```psj
        JPT.GetMaterialXML()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _String_ containing all the created user material in XML format.
        
        ## Sample Code
        
        ```psj {6}
        # Create user material data base
        Properties.Material.Add("Copper_Alloy", [Density([(DENSITY, 8.3e-09)]),
                                Elastic([(YOUNGS_MODULUS, 110000.0), (POISSONS_RATIO, 0.34)])])
        
        # Get all the created user material and store it in XML format
        createdMat = JPT.GetMaterialXML()
        pprint(createdMat)
        ```
        
        """
        message = "JPT.GetMaterialXML({})".format('')
        return JPT_RUN_LINE(message)

    def GetMaxIDEntity(DItemType):
        r"""
        ## Description
        
        Get the maximum ID of the inputted DItemType.
        
        ## Syntax
        
        ```psj
        JPT.GetMaxIDEntity(DItemType)
        ```
        
        ## Inputs
        
        ### `DItemType`
        
        - An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.
        - This is a required input.
        
        ## Return Code
        
        A _Integer_ specifying the maximum ID of the inputted DItemType.
        
        ## Sample Code
        
        ```psj {8}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Get the maximum ID of the created parts
        iMaxID = JPT.GetMaxIDEntity(JPT.DItemType.BODY)
        JPT.Debugger(iMaxID) # 3
        ```
        
        """
        message = "JPT.GetMaxIDEntity({})".format(DItemType)
        return JPT_RUN_LINE(message)

    def GetMaxMaterialID():
        r"""
        ## Description
        
        Get the maximum ID of the user material in the user material database.
        
        ## Syntax
        
        ```psj
        JPT.GetMaxMaterialID()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        An _Integer_ specifying the maximum ID of the user material in the user material database.
        
        ## Sample Code
        
        ```psj {10}
        # Create user material data base
        Properties.Material.Add("Stainless_Steel", [Density([(DENSITY, 7.75e-09)]),
                                Elastic([(YOUNGS_MODULUS, 193000.0), (POISSONS_RATIO, 0.31)])])
        Properties.Material.Add("Titanium_Alloy", [Density([(DENSITY, 4.62e-09)]),
                                Elastic([(YOUNGS_MODULUS, 96000.0), (POISSONS_RATIO, 0.36)])])
        Properties.Material.Add("Aluminum_Alloy", [Density([(DENSITY, 2.7699999999999997e-09)]),
                                Elastic([(YOUNGS_MODULUS, 71000.0), (POISSONS_RATIO, 0.33)])])
        
        # Get the maximum ID of the user material in the User material Database
        iMaxMaterialID = JPT.GetMaxMaterialID()
        JPT.Debugger(iMaxMaterialID) # Return an integer object with value = 3
        ```
        
        """
        message = "JPT.GetMaxMaterialID({})".format('')
        return JPT_RUN_LINE(message)

    def GetMaxResultCoord(bVisible =False):
        r"""
        ## Description
        
        Get coordinate of the node/center node of the element having the maximum value of the plotting result.
        
        ## Syntax
        
        ```psj
        JPT.GetMaxResultCoord(...)
        ```
        
        ## Inputs
        
        ### `bVisible `
        
        - An _Bool_ specifying whether to restrict the target to only visible entity (_True_) or not(_False_)
        - The default value is _False_.
        
        
        ## Return Code
        
        A _[DoubleVector](../data-type/psj-utility/pre-utility/built-in-types/DoubleVector)_ specifying the coordinate of the node/center node of the element (Based on the **Display At** type) having the maximum value of the plotting result.
        
        :::note
        
        In case the result has not been plotted yet, this utility will return a list = **[-1.79769e+308, -1.79769e+308, -1.79769e+308]**.
        
        :::
        
        ## Sample Code
        
        ```psj {11,20}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XY, 4}, {1, 1, 0, 0, 1, 8, 0, \
                                     0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, \
                                     0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, \
                                     0.000000, 0}, 0, 0)')
        
        # Get the coordinate of the node having the maximum value of the plotting result
        maxNodeCoord = JPT.GetMaxResultCoord()
        JPT.Debugger(maxNodeCoord)
        
        # Get the coordinate of the center of an element having the maximum value of the plotting result
        JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XY, 2}, {2, 1, 0, 0, 0, 0, \
                                     0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                                     0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, \
                                     0, 0, 0, 0.000000, 0}, 0, 0)')
        
        maxElemCenterCoord = JPT.GetMaxResultCoord()
        JPT.Debugger(maxElemCenterCoord)
        ```
        
        """
        message = "JPT.GetMaxResultCoord({})".format(bVisible )
        return JPT_RUN_LINE(message)

    def GetMaxResultId(bVisible =False):
        r"""
        ## Description
        
        Get the ID of the node/element having the maximum value of the plotting result.
        
        ## Syntax
        
        ```psj
        JPT.GetMaxResultId(...)
        ```
        
        ## Inputs
        
        ### `bVisible `
        
        - An _Bool_ specifying whether to restrict the target to only visible entity (_True_) or not(_False_)
        - The default value is _False_.
        
        ## Return Code
        
        An _Integer_ specifying the ID of the node/element (Based on the **Display At** type) having the maximum value of the plotting result.
        
        :::note
        
        In case the result has not been plotted yet, this utility will return **-1**.
        
        :::
        
        ## Sample Code
        
        ```psj {11,20}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XY, 4}, {1, 1, 0, 0, 1, 8, \
                                     0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                                     0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, \
                                     0, 0, 0, 0.000000, 0}, 0, 0)')
        
        # Get the ID of the node having the maximum value of the plotting result
        maxNodeID = JPT.GetMaxResultId()
        JPT.Debugger(maxNodeID)
        
        # Get the ID of the element having the maximum value of the plotting result
        JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XY, 2}, {2, 1, 0, 0, 0, 0, \
                                     0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                                     0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, \
                                     0, 0, 0, 0.000000, 0}, 0, 0)')
        
        maxElemID = JPT.GetMaxResultId()
        JPT.Debugger(maxElemID)
        ```
        
        """
        message = "JPT.GetMaxResultId({})".format(bVisible )
        return JPT_RUN_LINE(message)

    def GetMaxResultValue(bVisible =False):
        r"""
        ## Description
        
        Get the maximum value of the current plotting result.
        
        ## Syntax
        
        ```psj
        JPT.GetMaxResultValue(...)
        ```
        
        ## Inputs
        
        ### `bVisible `
        
        - An _Bool_ specifying whether to restrict the target to only visible entity (_True_) or not(_False_)
        - The default value is _False_.
        
        
        ## Return Code
        
        An _Integer_ specifying the maximum value of the plotting result.
        
        :::note
        
        In case the result has not been plotted yet, this utility will return **-1.7976931348623157e+308**.
        
        :::
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XY, 4}, {1, 1, 0, 0, 1, 8, \
                                     0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                                     0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, \
                                     0, 0, 0, 0.000000, 0}, 0, 0)')
        
        # Get the maximum value of the plotting result
        maxResult = JPT.GetMaxResultValue()
        JPT.Debugger(maxResult)
        ```
        
        """
        message = "JPT.GetMaxResultValue({})".format(bVisible )
        return JPT_RUN_LINE(message)

    def GetMinIDEntity(DItemType):
        r"""
        ## Description
        
        Get the minimum ID of the inputted DItemType.
        
        ## Syntax
        
        ```psj
        JPT.GetMinIDEntity(DItemType)
        ```
        
        ## Inputs
        
        ### `DItemType`
        
        - An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.
        - This is a required input.
        
        ## Return Code
        
        A _Integer_ specifying the maximum ID of the inputted DItemType.
        
        ## Sample Code
        
        ```psj {8}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Get the minimum ID of the created parts
        iMinID = JPT.GetMinIDEntity(JPT.DItemType.BODY)
        JPT.Debugger(iMinID) # 1
        ```
        
        """
        message = "JPT.GetMinIDEntity({})".format(DItemType)
        return JPT_RUN_LINE(message)

    def GetMinResultCoord(bVisible =False):
        r"""
        ## Description
        
        Get coordinate of the node/center node of the element having the minimum value of the plotting result.
        
        ## Syntax
        
        ```psj
        JPT.GetMinResultCoord(...)
        ```
        
        ## Inputs
        
        ### `bVisible `
        
        - An _Bool_ specifying whether to restrict the target to only visible entity (_True_) or not(_False_)
        - The default value is _False_.
        
        ## Return Code
        
        A _[DoubleVector](../data-type/psj-utility/pre-utility/built-in-types/DoubleVector)_ specifying the coordinate of the node/center node of the element (Based on the **Display At** type) having the minimum value of the plotting result.
        
        :::note
        
        In case the result has not been plotted yet, this utility will return a list = **[-1.79769e+308, -1.79769e+308, -1.79769e+308]**.
        
        :::
        
        ## Sample Code
        
        ```psj {11,20}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XY, 4}, {1, 1, 0, 0, 1, 8, 0, \
                                     0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, \
                                     0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, \
                                     0.000000, 0}, 0, 0)')
        
        # Get the coordinate of the node having the minimum value of the plotting result
        minNodeCoord = JPT.GetMinResultCoord()
        JPT.Debugger(minNodeCoord)
        
        # Get the coordinate of the center of an element having the minimum value of the plotting result
        JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XY, 2}, {2, 1, 0, 0, 0, 0, \
                                     0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                                     0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, \
                                     0, 0, 0, 0.000000, 0}, 0, 0)')
        
        minElemCenterCoord = JPT.GetMinResultCoord()
        JPT.Debugger(minElemCenterCoord)
        ```
        
        """
        message = "JPT.GetMinResultCoord({})".format(bVisible )
        return JPT_RUN_LINE(message)

    def GetMinResultId(bVisible =False):
        r"""
        ## Description
        
        Get the ID of the node/element having the minimum value of the plotting result.
        
        ## Syntax
        
        ```psj
        JPT.GetMinResultId(...)
        ```
        
        ## Inputs
        
        ### `bVisible `
        
        - An _Bool_ specifying whether to restrict the target to only visible entity (_True_) or not(_False_)
        - The default value is _False_.
        
        
        ## Return Code
        
        An _Integer_ specifying the ID of the node/element (Based on the **Display At** type) having the minimum value of the plotting result.
        
        :::note
        
        In case the result has not been plotted yet, this utility will return **-1**.
        
        :::
        
        ## Sample Code
        
        ```psj {11,20}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XY, 4}, {1, 1, 0, 0, 1, 8, \
                                     0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                                     0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, \
                                     0, 0, 0, 0.000000, 0}, 0, 0)')
        
        # Get the ID of the node having the minimum value of the plotting result
        minNodeID = JPT.GetMinResultId()
        JPT.Debugger(minNodeID)
        
        # Get the ID of the element having the minimum value of the plotting result
        JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XY, 2}, {2, 1, 0, 0, 0, 0, \
                                     0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                                     0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, \
                                     0, 0, 0, 0.000000, 0}, 0, 0)')
        
        minElemID = JPT.GetMinResultId()
        JPT.Debugger(minElemID)
        ```
        
        """
        message = "JPT.GetMinResultId({})".format(bVisible )
        return JPT_RUN_LINE(message)

    def GetMinResultValue():
        r"""
        ## Description
        
        Get the minimum value of the current plotting result.
        
        ## Syntax
        
        ```psj
        JPT.GetMinResultValue(...)
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        ### `bVisible `
        
        - An _Bool_ specifying whether to restrict the target to only visible entity (_True_) or not(_False_)
        - The default value is _False_.
        
        
        :::note
        
        In case the result has not been plotted yet, this utility will return **-1.7976931348623157e+308**.
        
        :::
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XY, 4}, {1, 1, 0, 0, 1, 8, \
                                     0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, \
                                     0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, \
                                     0, 0, 0, 0.000000, 0}, 0, 0)')
        
        # Get the minimum value of the plotting result
        minResult = JPT.GetMinResultValue()
        JPT.Debugger(minResult)
        ```
        
        """
        message = "JPT.GetMinResultValue({})".format('')
        return JPT_RUN_LINE(message)

    def GetNodeResult(PostDataRangeType, resultValue, tolerance=1E-5):
        r"""
        ## Description
        
        Get nodes with loaded results satisfy a condition.
        
        ## Syntax
        
        ```psj
        JPT.GetNodeResult(PostDataRangeType,
                             resultValue,
                             adjustment)
        ```
        
        ## Inputs
        
        ### `PostDataRangeType`
        
        - An _Enum_ specifying the _[PostDataRangeType](../data-type/psj-utility/post-utility/enumeration-types/post-data-range-types)_ describing the condition to get the nodal results.
        - This is a required input.
        
        ### `resultValue`
        
        - A _Double_ specifying the referenced value.
        - This is a required input.
        
        ### `tolerance`
        
        - A _Double_ specifying the adjustment to the base value _[resultValue](#resultvalue)_:
          - If _[PostDataRangeType](../data-type/psj-utility/post-utility/enumeration-types/post-data-range-types)_ is a scalar type (i.e. EQ, NE, LT, GT, LE, GE), then the range to get the result is from (resultValue - adjustment) to (resultValue + adjustment)
          - If _[PostDataRangeType](../data-type/psj-utility/post-utility/enumeration-types/post-data-range-types)_ is a range type (i.e. IR, OR, IRE, ORE), then the range to get the result is from (resultValue) to (adjustment)
        - The default value is 1E-5.
        
        ## Return Code
        
        A _List of Cursor_ containing nodes with loaded nodal results satisfy the given condition.
        
        ## Sample Code
        
        ```psj {10,14}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, Max Principal Stress, 4}, {1, 1, 0, 0, 1, 8, \
                                     0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, \
                                     0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')
        
        # Create a nodal group whose nodal results greater than 1 (tolerance=10E-3)
        list_node_1= JPT.GetNodeResult(JPT.PostDataRangeType.GT,1,10E-3)
        Tools.Group.CreateGroup(strGroupName="Group_Node_1", crlTargets=list_node_1)
        
        # Create a nodal group  whose nodal results in range (1,5)
        list_node_2= JPT.GetNodeResult(JPT.PostDataRangeType.IR,1,5)
        Tools.Group.CreateGroup(strGroupName="Group_Node_2", crlTargets=list_node_2)
        ```
        
        """
        message = "JPT.GetNodeResult({},{},{})".format(PostDataRangeType,resultValue,tolerance)
        return JPT_RUN_LINE(message)

    def GetOpnList():
        r"""
        ## Description
        
        Get a _List of String_ stores name of functions having their own GUI.
        
        ## Syntax
        
        ```psj
        JPT.GetOpnList()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[StringVector](../data-type/psj-utility/pre-utility/built-in-types/StringVector)_ specifying the functions having their own GUI.
        
        ## Sample Code
        
        ```psj {2}
        # Get all the functions having their own GUI
        allFuncsWithGUI = JPT.GetOpnList()
        JPT.Debugger(allFuncsWithGUI)
        JPT.Debugger(allFuncsWithGUI[3])
        ```
        
        """
        message = "JPT.GetOpnList({})".format('')
        return JPT_RUN_LINE(message)

    def GetOutputLog():
        r"""
        ## Description
        
        Get the text existing on the Output window.
        
        ## Syntax
        
        ```psj
        JPT.GetOutputLog()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _String_ containing all the text existing on the Output window.
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model to write all text on Output log
        Geometry.Part.Cube(strName="Cube_5", iPartColor=7463537)
        Geometry.Part.Cube(strName="Cube_6", iPartColor=7434735)
        Geometry.Part.Cube(strName="Cube_7", iPartColor=14903267)
        Geometry.Part.Cube(strName="Cube_8", iPartColor=15658599)
        Geometry.Part.Cube(strName="Cube_9", iPartColor=7961077)
        Geometry.Part.Cube(strName="Cube_10", iPartColor=7829501)
        JPT.ViewFitToModel()
        
        # Get the printed text in Output window
        log = JPT.GetOutputLog()
        JPT.Debugger(log)
        ```
        
        """
        message = "JPT.GetOutputLog({})".format('')
        return JPT_RUN_LINE(message)

    def GetPostElemFromPosition(xCoordValue, yCoordValue, zCoordValue, dTolerance, bVisible):
        r"""
        ## Description
        
        Get post element from a specific position.
        
        ## Syntax
        
        ```psj
        JPT.GetPostElemFromPosition(xCoordValue,
                                    yCoordValue,
                                    zCoordValue,
                                    dTolerance,
                                    bVisible)
        ```
        
        ## Inputs
        
        ### `xCoordValue`
        
        - A _Double_ specifying the value in X coordinate in millimeters [mm] in the Cartesian coordinate system..
        - This is a required input.
        
        ### `yCoordValue`
        
        - A _Double_ specifying the value in Y coordinate in millimeters [mm] in the Cartesian coordinate system..
        - This is a required input.
        
        ### `zCoordValue`
        
        - A _Double_ specifying the value in Z coordinate in millimeters [mm] in the Cartesian coordinate system.
        - This is a required input.
        
        ### `dTolerance`
        
        - A _Double_ specifying the tolerance to search the satisfying element in millimeters [mm]. This argument will help to find the first nearest element with the input position.
        - This is a required input.
        
        ### `bVisible`
        
        - A _Boolean_ specifying the search mode.
          - _True_: Only search for elements which is displayed on the screen
          - _False_: Enable to search in the hidden elements
        - This is a required input.
        
        ## Return Code
        
        A _[DPostElem](../data-type/psj-utility/post-utility/post-built-in-types/DPostElem)_ object containing the Post Element information.
        
        ## Sample Code
        
        ```psj {15}
        JPT.ClearLog()
        # Set up model path
        JupiterPath = JPT.GetAppPathInfo(JPT.PathType.PROGRAM_PATH)
        modelPath = JupiterPath + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        
        # Import result
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 1, 1, 1)'.format(modelPath))
        JPT.ViewFitToModel()
        
        # Show Result
        JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, Mises, 2}, {2, 0, 0, 0, 0, 0, 0, 0.000000, 0}, \
        0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, \
        {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')
        JPT.Exec('CmdShowPostDeformation(183:1, 1, 0, 1, 1, 0, 0.000000, 0, 0.070000, 0, 0.070000, 0.070000, 0.070000, 0)')
        
        # Get Element by position
        elemWith_Tolerance = JPT.GetPostElemFromPosition(16, 20, 5, 0.1, 1)
        JPT.Debugger(elemWith_Tolerance) #Element ID = 409
        ```
        
        """
        message = "JPT.GetPostElemFromPosition({},{},{},{},{})".format(xCoordValue,yCoordValue,zCoordValue,dTolerance,bVisible)
        return JPT_RUN_LINE(message)

    def GetPostResultAmt(PostAnalysisType, resultSet, timeStep, resultName, componentName, PostResultDataLoc):
        r"""
        ## Description
        
        Get Physical Amount information of the specify result.
        
        ## Syntax
        
        ```psj
        JPT.GetPostResultAmt(PostAnalysisType,
                             resultSet,
                             timeStep,
                             resultName,
                             componentName,
                             PostResultDataLoc)
        ```
        
        ## Inputs
        
        ### `PostAnalysisType`
        
        - An _Enum_ specifying the _[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.
        - This is a required input.
        
        ### `resultSet`
        
        - An _Integer_ specifying the step ID of the imported result.
        - This is a required input.
        
        ### `timeStep`
        
        - An _Integer_ specifying the time step of the imported result.
        - This is a required input.
        
        ### `resultName`
        
        - A _String_ specifying the type of result (Such as Displacement, Stress, etc.).
        - This is a required input.
        
        ### `componentName`
        
        - A _String_ specifying a specific direction of the result (Such as X, Y, Z, etc.).
        - This is a required input.
        
        ### `PostResultDataLoc`
        
        - An _Enum_ specifying the _[PostResultDataLoc](../data-type/psj-utility/post-utility/enumeration-types/post-result-data-loc-types)_ describing the location of result (Such as on node, on element, etc.).
        - This is a required input.
        
        ## Return Code
        
        An _Integer_ specifying the [Physical Amount](../data-type/psj-utility/post-utility/enumeration-types/post-result-data-amt-types) type of the working result.
        
        ## Sample Code
        
        ```psj {6-11}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, \
                                       1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        amt_info = JPT.GetPostResultAmt(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,
                                       1,
                                       1,
                                       "Stress",
                                       "XX",
                                       JPT.PostResultDataLoc.POST_LOC_ON_ELEMENT_NODE)
        JPT.Debugger(amt_info)
        ```
        
        """
        message = "JPT.GetPostResultAmt({},{},{},{},{},{})".format(PostAnalysisType,resultSet,timeStep,resultName,componentName,PostResultDataLoc)
        return JPT_RUN_LINE(message)

    def GetPostSolverType():
        r"""
        ## Description
        
        Get the result type of the current importing result file.
        
        ## Syntax
        
        ```psj
        JPT.GetPostSolverType()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        An _Enum_ specifying the [Post Job type](../data-type/psj-utility/post-utility/enumeration-types/post-job-types) of importing result.
        
        ## Sample Code
        
        ```psj {6}
        # Prepare Post model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
        Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
        
        # Get Post Job type
        type = JPT.GetPostSolverType()
        print(type)
        ```
        
        """
        message = "JPT.GetPostSolverType({})".format('')
        return JPT_RUN_LINE(message)

    def GetPostSolverTypeString():
        r"""
        ## Description
        
        Get solver type of the current importing result.
        
        ## Syntax
        
        ```psj
        JPT.GetPostSolverTypeString()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _String_ specifying the name of solver type (Such as Nastran OP2, Nastran HDF5, ADVC, Abaqus, etc).
        
        ## Sample Code
        
        ```psj {5}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        strSolverType = JPT.GetPostSolverTypeString()
        JPT.Debugger(strSolverType)
        ```
        
        """
        message = "JPT.GetPostSolverTypeString({})".format('')
        return JPT_RUN_LINE(message)

    def GetProgramPath():
        r"""
        ## Description
        
        Get the path to the current Jupiter installation folder.
        
        ## Syntax
        
        ```psj
        JPT.GetProgramPath()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        The path to the current Jupiter installation folder.
        
        ## Sample Code
        
        ```psj {2}
        # Get the current Jupiter installation folder
        path = JPT.GetProgramPath()
        JPT.Debugger(path)
        ```
        
        """
        message = "JPT.GetProgramPath({})".format('')
        return JPT_RUN_LINE(message)

    def GetProgramVersion():
        r"""
        ## Description
        
        Get all the version information of the current Jupiter application.
        
        ## Syntax
        
        ```psj
        JPT.GetProgramVersion()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[VersionInfo](../data-type/psj-utility/pre-utility/built-in-types/VersionInfo)_ object specifying a _List_ containing the version, revision information of the current Jupiter application, including:
        
        - Major
        - Minor
        - Sub
        - Build.
        
        ## Sample Code
        
        ```psj {2}
        # Get the version information of the current Jupiter
        version = JPT.GetProgramVersion()
        print(f"Jupiter {version.major}.{version.minor}.{version.sub}")
        print(f"Revision {version.build}")
        ```
        
        """
        message = "JPT.GetProgramVersion({})".format('')
        return JPT_RUN_LINE(message)

    def GetPythonAPILog():
        r"""
        ## Description
        
        Get the text existing on the Python API window.
        
        ## Syntax
        
        ```psj
        JPT.GetPythonAPILog()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _String_ containing all the text existing on the Python API window.
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model to write all text on Python API log
        Geometry.Part.Cube(strName="Cube_5", iPartColor=7463537)
        Geometry.Part.Cube(strName="Cube_6", iPartColor=7434735)
        Geometry.Part.Cube(strName="Cube_7", iPartColor=14903267)
        Geometry.Part.Cube(strName="Cube_8", iPartColor=15658599)
        Geometry.Part.Cube(strName="Cube_9", iPartColor=7961077)
        Geometry.Part.Cube(strName="Cube_10", iPartColor=7829501)
        JPT.ViewFitToModel()
        
        # Get the printed text in Python API window
        log = JPT.GetPythonAPILog()
        JPT.Debugger(log)
        ```
        
        """
        message = "JPT.GetPythonAPILog({})".format('')
        return JPT_RUN_LINE(message)

    def GetRandomJPTColor():
        r"""
        ## Description
        
        Get random color code in Jupiter.
        
        ## Syntax
        
        ```psj
        JPT.GetRandomJPTColor()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        An _Integer_ specifying a color code in Jupiter.
        
        ## Sample Code
        
        ```psj {2}
        # Get a random color code in Jupiter
        color = JPT.GetRandomJPTColor()
        JPT.Debugger(color)
        ```
        
        """
        message = "JPT.GetRandomJPTColor({})".format('')
        return JPT_RUN_LINE(message)

    def GetRedoCount():
        r"""
        ## Description
        
        Get the total number of Redo which is capable for executing.
        
        ## Syntax
        
        ```psj
        JPT.GetRedoCount()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        An _Integer_ specifying the number of Redo operation.
        
        ## Sample Code
        
        ```psj {12}
        # Prepare model and redo steps
        Geometry.Part.Cube(strName="Cube_11", iPartColor=11842649)
        Geometry.Part.Cube(strName="Cube_12", iPartColor=14968422)
        Geometry.Part.Cube(strName="Cube_13", iPartColor=6250447)
        Geometry.Part.Cube(strName="Cube_14", iPartColor=12734402)
        Geometry.Part.Cube(strName="Cube_15", iPartColor=16579696)
        Geometry.Part.Cube(strName="Cube_16", iPartColor=7666683)
        Geometry.Part.Cube(strName="Cube_17", iPartColor=12867524)
        Toolbar.Undo(iCntUndo=3)
        
        # Get the number of the available Redo
        iRedoSteps = JPT.GetRedoCount()
        JPT.Debugger(iRedoSteps) # Return an integer object with value = 3
        ```
        
        """
        message = "JPT.GetRedoCount({})".format('')
        return JPT_RUN_LINE(message)

    def GetResultByElemId(elementID):
        r"""
        ## Description
        
        Get the result value of specified Element by ID.
        If multiple result data are retrieved (e.g., Mises & Principal), please use JPT.GetAllResultsByElemId.
        
        ## Syntax
        
        ```psj
        JPT.GetResultByElemId(elementID)
        ```
        
        ## Inputs
        
        ### `elementID`
        
        - An _Integer_ specifying the ID of Element to be checked the result value.
        - This is a required input.
        
        ## Return Code
        
        A _Double_ specifying the result of Element.
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XX, 2}, {2, 1, 0, 0, 0, 0, 0, \
                                     0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, \
                                     0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, {0, 0, 0, 0, 0, 0, 0, \
                                     0.000000, 0}, 0, 0)')
        
        # Get the result value of Element ID = 658
        valueElementID = JPT.GetResultByElemId(658)
        print("Stress of XX component of Element ID = 658: " + str(valueElementID))
        ```
        
        """
        message = "JPT.GetResultByElemId({})".format(elementID)
        return JPT_RUN_LINE(message)

    def GetResultByNodeId(nodeID):
        r"""
        ## Description
        
        Get the result value of specified Node by ID.
        If multiple result data are retrieved (e.g., Mises & Principal), please use JPT.GetAllResultsByNodeId.
        
        ## Syntax
        
        ```psj
        JPT.GetResultByNodeId(nodeID)
        ```
        
        ## Inputs
        
        ### `nodeID`
        
        - An _Integer_ specifying the ID of Node to be checked the result value.
        - This is a required input.
        
        ## Return Code
        
        A _Double_ specifying the result of Node.
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Displacement, X, 1}, {1, 1, 0, \
                                     0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, \
                                     {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, \
                                     {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')
        
        # Get the result value of Node ID = 62
        valueNodeID = JPT.GetResultByNodeId(62)
        print("Displacement of X component of Node ID = 62: " + str(valueNodeID))
        ```
        
        """
        message = "JPT.GetResultByNodeId({})".format(nodeID)
        return JPT_RUN_LINE(message)

    def GetResultComponentNames(PostAnalysisType, resultSet, timeStep, resultName, BoolType):
        r"""
        ## Description
        
        Get all the available result directions of the inputted result type.
        
        ## Syntax
        
        ```psj
        JPT.GetResultComponentNames(PostAnalysisType,
                                    resultSet,
                                    timeStep,
                                    resultName,
                                    BoolType)
        ```
        
        ## Inputs
        
        ### `PostAnalysisType`
        
        - An _Enum_ specifying the _[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.
        - This is a required input.
        
        ### `resultSet`
        
        - An _Integer_ specifying the step ID of the imported result.
        - This is a required input.
        
        ### `timeStep`
        
        - An _Integer_ specifying the time step of the imported result.
        - This is a required input.
        
        ### `resultName`
        
        - A _String_ specifying the type of result (Such as Displacement, Stress, etc.).
        - This is a required input.
        
        ### `BoolType`
        
        - An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the selection:
          - _True_: Select the inputted entity with its ID.
          - _False_: Deselect the inputted entity with its ID.
        - This is a required input.
        
        ## Return Code
        
        A _List of String_ containing all the available data directions of the inputted result type.
        
        ## Sample Code
        
        ```psj {5-10}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        steps=JPT.GetResultSteps()
        for step in steps:
            incs=JPT.GetResultIncrements(step.first, step.third)
            for inc in incs:
                result_comp_name = JPT.GetResultComponentNames(step.first,     # analysis type
                                                               step.third,     # result set
                                                               inc,            # time step
                                                               "Displacement", # result name
                                                               JPT.BoolType.TRUE_VAL)
        
                JPT.Debugger(result_comp_name)
        
        ```
        
        """
        message = "JPT.GetResultComponentNames({},{},{},{},{})".format(PostAnalysisType,resultSet,timeStep,resultName,BoolType)
        return JPT_RUN_LINE(message)

    def GetResultIncrements(PostAnalysisType, resultSet):
        r"""
        ## Description
        
        Get all the existing increments of the inputted result step.
        
        ## Syntax
        
        ```psj
        JPT.GetResultIncrements(PostAnalysisType,
                                resultSet)
        ```
        
        ## Inputs
        
        ### `PostAnalysisType`
        
        - An _Enum_ specifying the _[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.
        - This is a required input.
        
        ### `resultSet`
        
        - An _Integer_ specifying the step ID of the imported result.
        - This is a required input.
        
        ## Return Code
        
        A _List of Integer_ containing all the existing increments of the inputted result type with it's step.
        
        ## Sample Code
        
        ```psj {5-8}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        result_increments = \
            JPT.GetResultIncrements(JPT.PostAnalysisType.POST_ANALYSIS_MODAL,
                                    1)
        
        JPT.Debugger(result_increments)
        ```
        
        """
        message = "JPT.GetResultIncrements({},{})".format(PostAnalysisType,resultSet)
        return JPT_RUN_LINE(message)

    def GetResultLocations(PostAnalysisType, resultSet, timeStep, resultName, componentName):
        r"""
        ## Description
        
        Get all the available data location existing on the inputted result type and direction.
        
        ## Syntax
        
        ```psj
        JPT.GetResultLocations(PostAnalysisType,
                               resultSet,
                               timeStep,
                               resultName,
                               componentName)
        ```
        
        ## Inputs
        
        ### `PostAnalysisType`
        
        - An _Enum_ specifying the _[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.
        - This is a required input.
        
        ### `resultSet`
        
        - An _Integer_ specifying the step ID of the imported result.
        - This is a required input.
        
        ### `timeStep`
        
        - An _Integer_ specifying the time step of the imported result.
        - This is a required input.
        
        ### `resultName`
        
        - A _String_ specifying the type of result (Such as Displacement, Stress, etc.).
        - This is a required input.
        
        ### `componentName`
        
        - A _String_ specifying a specific direction of the result (Such as X, Y, Z, etc.).
        - This is a required input.
        
        ## Return Code
        
        A _List of Integer_ containing all the available [PostResultDataLoc](../data-type/psj-utility/post-utility/enumeration-types/post-result-data-loc-types) of the inputted result type and it's direction.
        
        ## Sample Code
        
        ```psj {5-11}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        result_location = \
            JPT.GetResultLocations(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,
                                   1,
                                   1,
                                   "Stress",
                                   "XX")
        
        JPT.Debugger(result_location)
        #2: JPT.PostResultDataLoc.POST_LOC_ON_ELEMENT
        #4: JPT.PostResultDataLoc.POST_LOC_ON_ELEMENT_NODE
        ```
        
        """
        message = "JPT.GetResultLocations({},{},{},{},{})".format(PostAnalysisType,resultSet,timeStep,resultName,componentName)
        return JPT_RUN_LINE(message)

    def GetResultNames(PostAnalysisType, resultSet, timeStep, BoolType):
        r"""
        ## Description
        
        Get all the available result type existing on the model.
        
        ## Syntax
        
        ```psj
        JPT.GetResultNames(PostAnalysisType,
                           resultSet,
                           timeStep,
                           BoolType)
        ```
        
        ## Inputs
        
        ### `PostAnalysisType`
        
        - An _Enum_ specifying the _[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.
        - This is a required input.
        
        ### `resultSet`
        
        - An _Integer_ specifying the step ID of the imported result.
        - This is a required input.
        
        ### `timeStep`
        
        - An _Integer_ specifying the time step of the imported result.
        - This is a required input.
        
        ### `BoolType`
        
        - An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ specifying whether to use the name of the current language setting.
          - _True_: Use the name of the current language setting.
          - _False_: Use the English name.
        - This is a required input.
        
          :::tip
          You also can input **1** or **True** instead of inputting JPT.BoolType.TRUE_VAL  
          You also can input **0** or **False** instead of inputting JPT.BoolType.FALSE_VAL
          :::
        
        ## Return Code
        
        A _List of String_ containing all the available result types existing on the model.
        
        ## Sample Code
        
        ```psj {5-9}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        #Get All Result Names in all steps and increments
        steps=JPT.GetResultSteps()
        for step in steps:
            incs=JPT.GetResultIncrements(step.first, step.third)
            for inc in incs:
                result_name = JPT.GetResultNames(step.first,    #analysis type
                                                 step.third,    #result set
                                                 inc,           #time step
                                                 JPT.BoolType.TRUE_VAL)
        
                JPT.Debugger(result_name)
        ```
        
        """
        message = "JPT.GetResultNames({},{},{},{})".format(PostAnalysisType,resultSet,timeStep,BoolType)
        return JPT_RUN_LINE(message)

    def GetResultSetName(PostAnalysisType, resultSet):
        r"""
        ## Description
        
        Get the name of Result Set (Subcase).
        
        ## Syntax
        
        ```psj
        JPT.GetResultSetName(PostAnalysisType,
                             resultSet)
        ```
        
        ## Inputs
        
        ### `PostAnalysisType`
        
        - An _Enum_ specifying the _[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.
        - This is a required input.
        
        ### `resultSet`
        
        - An _Integer_ specifying the step ID of the imported result.
        - This is a required input.
        
        ## Return Code
        
        A _String_ specifying the name of Result Set (Subcase).
        
        ## Sample Code
        
        ```psj {5}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        result_set_name = JPT.GetResultSetName(1,1)
        JPT.Debugger(result_set_name)
        ```
        
        """
        message = "JPT.GetResultSetName({},{})".format(PostAnalysisType,resultSet)
        return JPT_RUN_LINE(message)

    def GetResultSetNameWithAnalysisID(PostAnalysisType, analysisID, resultSet):
        r"""
        ## Description
        
        Get the name of Result Set (Subcase).
        
        ## Syntax
        
        ```psj
        JPT.GetResultSetNameWithAnalysisID(PostAnalysisType,
                             analysisID,
                             resultSet)
        ```
        
        ## Inputs
        
        ### `PostAnalysisType`
        
        - An _Enum_ specifying the _[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.
        - This is a required input.
        
        ### `analysisID`
        
        - An _Integer_ specifying the analysis ID of the imported result.
        - This is a required input.
        
        ### `resultSet`
        
        - An _Integer_ specifying the step ID of the imported result.
        - This is a required input.
        
        ## Return Code
        
        A _String_ specifying the name of Result Set (Subcase).
        
        ## Sample Code
        
        ```psj {5}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        result_set_name = JPT.GetResultSetNameWithAnalysisID(1,0,1)
        JPT.Debugger(result_set_name)
        ```
        
        """
        message = "JPT.GetResultSetNameWithAnalysisID({},{},{})".format(PostAnalysisType,analysisID,resultSet)
        return JPT_RUN_LINE(message)

    def GetResultSteps():
        r"""
        ## Description
        
        Get all the existing result types and their time steps of the current result.
        
        ## Syntax
        
        ```psj
        JPT.GetResultSteps()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _List of Integer Triple_ containing information of result types, id and their steps.
        
        :::note
        
        To get their output values, you can use the below code (as an example):
        
        ```psj
        result_types_steps = JPT.GetResultSteps()
        for item in result_types_steps:
            result_type = item.first
            result_id = item.second
            result_step = item.third
            print("Result type: " + str(result_type))
            print("Result ID: " + str(result_id))
            print("Result step: " + str(result_step))
        ```
        
        For your reference, to printout all the properties and methods of the **JPT.GetResultSteps()** API, you can use **print(dir(JPT.GetResultSteps()))**.
        
        Besides, the output value is an integer number that specifying the result type. So, for checking the available result type, you can refer to **[PostAnalysisTypes](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)**.
        
        :::
        
        ## Sample Code
        
        ```psj {5}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        result_types_steps = JPT.GetResultSteps()
        
        print("Result type: " + str(result_types_steps[0].first)) #2: JPT.PostAnalysisType.POST_ANALYSIS_MODAL
        print("Result ID: " + str(result_types_steps[0].second))
        print("Result step: " + str(result_types_steps[0].third))
        ```
        
        """
        message = "JPT.GetResultSteps({})".format('')
        return JPT_RUN_LINE(message)

    def GetResultTimeStepInfo(PostAnalysisType, resultSet, timeStep):
        r"""
        ## Description
        
        Get the relating information of the inputted result step with it's time step.
        
        ## Syntax
        
        ```psj
        JPT.GetResultTimeStepInfo(PostAnalysisType,
                                  resultSet,
                                  timeStep)
        ```
        
        ## Inputs
        
        ### `PostAnalysisType`
        
        - An _Enum_ specifying the _[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.
        - This is a required input.
        
        ### `resultSet`
        
        - An _Integer_ specifying the step ID of the imported result.
        - This is a required input.
        
        ### `timeStep`
        
        - An _Integer_ specifying the time step of the imported result.
        - This is a required input.
        
        ## Return Code
        
        A _[PostTimeStepInfo](../data-type/psj-utility/post-utility/post-built-in-types/post-time-step-info)_ object specifying the information relating to the inputted time step.
        
        ## Sample Code
        
        ```psj {5-8}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        result_time_step_info = JPT.GetResultTimeStepInfo(JPT.PostAnalysisType.POST_ANALYSIS_MODAL,
                                                   1,
                                                   10)
        
        JPT.Debugger(result_time_step_info)
        
        print(result_time_step_info.mode)
        print(result_time_step_info.time)
        print(result_time_step_info.freq)
        ```
        
        """
        message = "JPT.GetResultTimeStepInfo({},{},{})".format(PostAnalysisType,resultSet,timeStep)
        return JPT_RUN_LINE(message)

    def GetResultTitle():
        r"""
        ## Description
        
        Get contents of title when result is loaded.
        
        ## Syntax
        
        ```psj
        JPT.GetResultTitle()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _Dictionary_ containing all the information of title.
        
        ## Sample Code
        
        ```psj {17}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        #Load result and deformation.
        JPT.Exec('CmdShowPostContour(183:1, \
                {2, 0, 1, 6, Displacement, Translational, 1}, \
                {1, 1, 0, 0, 0, 0, 0, 0.000000, 0}, 0, \
                {0, 0, 0, 0, , , 0}, \
                {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, \
                {0, 0, 0, 0, , , 0}, \
                {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')
        JPT.Exec('CmdShowPostDeformation(183:1, 2, 0, 1, 6, Displacement, Translational, \
                0, 0.000000, 0, 0.070000, 0, 0.070000, 0.070000, 0.070000, 0)')
        JPT.Exec('CmdEnableMiddleNodes(1)')
        
        title=JPT.GetResultTitle()
        pprint(title)
        ```
        
        """
        message = "JPT.GetResultTitle({})".format('')
        return JPT_RUN_LINE(message)

    def GetResultUseIncrement(PostAnalysisType, resultSet):
        r"""
        ## Description
        
        Check whether the result has any increment or not.
        
        ## Syntax
        
        ```psj
        JPT.GetResultUseIncrement(PostAnalysisType,
                                  resultSet)
        ```
        
        ## Inputs
        
        ### `PostAnalysisType`
        
        - An _Enum_ specifying the _[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.
        - This is a required input.
        
        ### `resultSet`
        
        - An _Integer_ specifying the step ID of the imported result.
        - This is a required input.
        
        ## Return Code
        
        A _Boolean_ specifying the existence of the increment of the inputted time step.
        
        ## Sample Code
        
        ```psj {5-6}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        is_increment_exist = \
            JPT.GetResultUseIncrement(JPT.PostAnalysisType.POST_ANALYSIS_MODAL, 1)
        
        JPT.Debugger(is_increment_exist)
        ```
        
        """
        message = "JPT.GetResultUseIncrement({},{})".format(PostAnalysisType,resultSet)
        return JPT_RUN_LINE(message)

    def GetScreenHeight():
        r"""
        ## Description
        
        Get the height of screen window.
        
        ## Syntax
        
        ```psj
        JPT.GetScreenHeight()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        An _Integer_ specifying the height value of Main Window.
        
        ## Sample Code
        
        ```psj {1}
        height=JPT.GetScreenHeight()
        JPT.Debugger(height)
        ```
        
        """
        message = "JPT.GetScreenHeight({})".format('')
        return JPT_RUN_LINE(message)

    def GetScreenPositionOfEntities(DItemVector):
        r"""
        ## Description
        
        Obtains the position of the specified item in the Main Window in screen coordinate system [min_x,min_y,max_x,max_y].
        
        ## Syntax
        
        ```psj
        JPT.GetScreenPositionOfEntities(...)
        ```
        
        ## Inputs
        
        ### `DItemVector`
        
        - A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object representing the item whose position on the Main Window is to be retrieved.
        - This is a required input.
        
        ## Return Code
        
        A list of_[int]_ representing the upper left and lower right coordinates of the area. If no item found on the Main Window, it returns a blank list.
        
        ## Sample Code
        
        ```psj {7}
        # Prepare model
        Geometry.Part.Cube(iPartColor=13290083)
        Geometry.Part.Cube(dlOrigin=[0.012, 0.0, 0.0], strName="Cube_2", iPartColor=6149981)
        JPT.ViewFitToModel()
        
        # Check screen position of parts in Main Window.
        ditem_list=JPT.GetAllByTypeID(JPT.DItemType.BODY)
        pos=JPT.GetScreenPositionOfEntities(ditem_list)
        JPT.Debugger(pos)
        ```
        
        """
        message = "JPT.GetScreenPositionOfEntities({})".format(DItemVector)
        return JPT_RUN_LINE(message)

    def GetScreenWidth():
        r"""
        ## Description
        
        Get the width of screen window.
        
        ## Syntax
        
        ```psj
        JPT.GetScreenWidth()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        An _Integer_ specifying the width value of Main Window.
        
        ## Sample Code
        
        ```psj {1}
        width=JPT.GetScreenWidth()
        JPT.Debugger(width)
        ```
        
        """
        message = "JPT.GetScreenWidth({})".format('')
        return JPT_RUN_LINE(message)

    def GetSelectedEdges():
        r"""
        ## Description
        
        Get all information of the selected edges.
        
        ## Syntax
        
        ```psj
        JPT.GetSelectedEdges()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        An _[EdgeVector](../data-type/psj-utility/pre-utility/built-in-types/EdgeVector)_ object or _List of [DEdge](../data-type/psj-utility/pre-utility/built-in-types/DEdge)_ objects containing all the information of the selected edges.
        
        ## Sample Code
        
        ```psj {13}
        # Prepare model
        Geometry.Part.Cube(iPartColor=7138156)
        Geometry.Part.Cube(strName="Cube_2", iPartColor=5921475)
        Geometry.Part.Cube(strName="Cube_3", iPartColor=6678117)
        Geometry.Part.Cube(strName="Cube_4", iPartColor=11908427)
        Geometry.Part.Cube(strName="Cube_5", iPartColor=15429611)
        Geometry.Part.Cube(strName="Cube_6", iPartColor=7531634)
        Geometry.Part.Cube(strName="Cube_7", iPartColor=12434775)
        Home.Find(strSearch="87 90 91 94 95 96 97 98", strSelectedType="Edge")
        JPT.ViewFitToModel()
        
        # Get the information of all selected edges
        listSelEdges = JPT.GetSelectedEdges()
        JPT.Debugger(listSelEdges)
        JPT.Debugger(listSelEdges[3])
        ```
        
        """
        message = "JPT.GetSelectedEdges({})".format('')
        return JPT_RUN_LINE(message)

    def GetSelectedEdgesCr():
        r"""
        ## Description
        
        Get all information of the selected edges under _List of Cursor_ format.
        
        ## Syntax
        
        ```psj
        JPT.GetSelectedEdgesCr()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _String_ specifying a cursor list (Macro string type) containing typeID and ID of the selected edges.
        
        ## Sample Code
        
        ```psj {13}
        # Prepare model
        Geometry.Part.Cube(iPartColor=7138156)
        Geometry.Part.Cube(strName="Cube_2", iPartColor=5921475)
        Geometry.Part.Cube(strName="Cube_3", iPartColor=6678117)
        Geometry.Part.Cube(strName="Cube_4", iPartColor=11908427)
        Geometry.Part.Cube(strName="Cube_5", iPartColor=15429611)
        Geometry.Part.Cube(strName="Cube_6", iPartColor=7531634)
        Geometry.Part.Cube(strName="Cube_7", iPartColor=12434775)
        Home.Find(strSearch="87 90 91 94 95 96 97 98", strSelectedType="Edge")
        JPT.ViewFitToModel()
        
        # Get the information of all selected edges
        listCursorSelEdges = JPT.GetSelectedEdgesCr()
        JPT.Debugger(listCursorSelEdges)
        ```
        
        """
        message = "JPT.GetSelectedEdgesCr({})".format('')
        return JPT_RUN_LINE(message)

    def GetSelectedElemEdges():
        r"""
        ## Description
        
        Get all information of the selected element edges.
        
        ## Syntax
        
        ```psj
        JPT.GetSelectedElemEdges()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[DItemPairVector](../data-type/psj-utility/pre-utility/built-in-types/DItemPairVector)_ object or _List of [DItemPair](../data-type/psj-utility/pre-utility/built-in-types/DItemPair)_ objects containing information of the selected element edges under _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ format.
        
        ## Sample Code
        
        ```psj {6}
        # Get the information of the selected element edges.
        # This function returns a list of DItemPair objects or DItemPairVetor object storing
        # information of element edges in DItem format
        # Element edges are not actual entity but defined by connection of 2 nodes.
        
        listSelElemEdges = JPT.GetSelectedElemEdges()
        for i in listSelElemEdges:
            print ('1st Node: {}'.format(i.firstDItem.id))
            print ('2nd Node: {}'.format(i.secondDItem.id))
        ```
        
        """
        message = "JPT.GetSelectedElemEdges({})".format('')
        return JPT_RUN_LINE(message)

    def GetSelectedElems():
        r"""
        ## Description
        
        Get all information of the selected elements.
        
        ## Syntax
        
        ```psj
        JPT.GetSelectedElems()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        An _[ElemVector](../data-type/psj-utility/pre-utility/built-in-types/EdgeVector)_ object or _List of [DElem](../data-type/psj-utility/pre-utility/built-in-types/DElem)_ objects containing all the information of the selected elements.
        
        ## Sample Code
        
        ```psj {14}
        # Prepare model
        Geometry.Part.Cube(iPartColor=7138156)
        Geometry.Part.Cube(strName="Cube_2", iPartColor=5921475)
        Geometry.Part.Cube(strName="Cube_3", iPartColor=6678117)
        Geometry.Part.Cube(strName="Cube_4", iPartColor=11908427)
        Geometry.Part.Cube(strName="Cube_5", iPartColor=15429611)
        Geometry.Part.Cube(strName="Cube_6", iPartColor=7531634)
        Geometry.Part.Cube(strName="Cube_7", iPartColor=12434775)
        Home.Find(strSearch="3199 3204 3201 3202 3200 3203 3186 3185 3183 3184 3181",
                  strSelectedType="2D Element")
        JPT.ViewFitToModel()
        
        # Get the information of all selected elements
        listSelElems = JPT.GetSelectedElems()
        JPT.Debugger(listSelElems)
        JPT.Debugger(listSelElems[2])
        ```
        
        """
        message = "JPT.GetSelectedElems({})".format('')
        return JPT_RUN_LINE(message)

    def GetSelectedElemsCr():
        r"""
        ## Description
        
        Get all information of the selected elements under _List of Cursor_ format.
        
        ## Syntax
        
        ```psj
        JPT.GetSelectedElemsCr()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _String_ specifying a cursor list (Macro string type) containing typeID and ID of the selected elements.
        
        ## Sample Code
        
        ```psj {14}
        # Prepare model
        Geometry.Part.Cube(iPartColor=7138156)
        Geometry.Part.Cube(strName="Cube_2", iPartColor=5921475)
        Geometry.Part.Cube(strName="Cube_3", iPartColor=6678117)
        Geometry.Part.Cube(strName="Cube_4", iPartColor=11908427)
        Geometry.Part.Cube(strName="Cube_5", iPartColor=15429611)
        Geometry.Part.Cube(strName="Cube_6", iPartColor=7531634)
        Geometry.Part.Cube(strName="Cube_7", iPartColor=12434775)
        Home.Find(strSearch="3199 3204 3201 3202 3200 3203 3186 3185 3183 3184 3181",
                  strSelectedType="2D Element")
        JPT.ViewFitToModel()
        
        # Get the information of all selected elements
        listCursorSelElems = JPT.GetSelectedElemsCr()
        JPT.Debugger(listCursorSelElems)
        ```
        
        """
        message = "JPT.GetSelectedElemsCr({})".format('')
        return JPT_RUN_LINE(message)

    def GetSelectedFaces():
        r"""
        ## Description
        
        Get all information of the selected faces.
        
        ## Syntax
        
        ```psj
        JPT.GetSelectedFaces()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[FaceVector](../data-type/psj-utility/pre-utility/built-in-types/FaceVector)_ object or _List of [DFace](../data-type/psj-utility/pre-utility/built-in-types/DFace)_ objects containing all the information of the selected faces.
        
        ## Sample Code
        
        ```psj {13}
        # Prepare model
        Geometry.Part.Cube(iPartColor=7138156)
        Geometry.Part.Cube(strName="Cube_2", iPartColor=5921475)
        Geometry.Part.Cube(strName="Cube_3", iPartColor=6678117)
        Geometry.Part.Cube(strName="Cube_4", iPartColor=11908427)
        Geometry.Part.Cube(strName="Cube_5", iPartColor=15429611)
        Geometry.Part.Cube(strName="Cube_6", iPartColor=7531634)
        Geometry.Part.Cube(strName="Cube_7", iPartColor=12434775)
        Home.Find(strSearch="20 21 22 23 24", strSelectedType="Face")
        JPT.ViewFitToModel()
        
        # Get the information of all selected edges
        listSelFaces = JPT.GetSelectedFaces()
        JPT.Debugger(listSelFaces)
        JPT.Debugger(listSelFaces[2])
        ```
        
        """
        message = "JPT.GetSelectedFaces({})".format('')
        return JPT_RUN_LINE(message)

    def GetSelectedFacesCr():
        r"""
        ## Description
        
        Get all information of the selected faces under _List of Cursor_ format.
        
        ## Syntax
        
        ```psj
        JPT.GetSelectedFacesCr()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _String_ specifying a cursor list (Macro string type) containing typeID and ID of the selected faces.
        
        ## Sample Code
        
        ```psj {13}
        # Prepare model
        Geometry.Part.Cube(iPartColor=7138156)
        Geometry.Part.Cube(strName="Cube_2", iPartColor=5921475)
        Geometry.Part.Cube(strName="Cube_3", iPartColor=6678117)
        Geometry.Part.Cube(strName="Cube_4", iPartColor=11908427)
        Geometry.Part.Cube(strName="Cube_5", iPartColor=15429611)
        Geometry.Part.Cube(strName="Cube_6", iPartColor=7531634)
        Geometry.Part.Cube(strName="Cube_7", iPartColor=12434775)
        Home.Find(strSearch="20 21 22 23 24", strSelectedType="Face")
        JPT.ViewFitToModel()
        
        # Get the information of all selected edges
        listCursorSelFaces = JPT.GetSelectedFacesCr()
        JPT.Debugger(listCursorSelFaces)
        ```
        
        """
        message = "JPT.GetSelectedFacesCr({})".format('')
        return JPT_RUN_LINE(message)

    def GetSelectedGroups():
        r"""
        ## Description
        
        Get all information of the selected groups.
        
        ## Syntax
        
        ```psj
        JPT.GetSelectedGroups()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[GroupVector](../data-type/psj-utility/pre-utility/built-in-types/GroupVector)_ object or _List of [DGroup](../data-type/psj-utility/pre-utility/built-in-types/DGroup)_ objects containing all the information of the selected groups.
        
        ## Sample Code
        
        ```psj {18}
        # Prepare model
        Geometry.Part.Cube(iPartColor=7138156)
        Geometry.Part.Cube(strName="Cube_2", iPartColor=5921475)
        Geometry.Part.Cube(strName="Cube_3", iPartColor=6678117)
        Geometry.Part.Cube(strName="Cube_4", iPartColor=11908427)
        Geometry.Part.Cube(strName="Cube_5", iPartColor=15429611)
        Geometry.Part.Cube(strName="Cube_6", iPartColor=7531634)
        Geometry.Part.Cube(strName="Cube_7", iPartColor=12434775)
        Tools.Group.CreateGroup(strGroupName="FaceGroup1", crlTargets=[Face(130)])
        Tools.Group.CreateGroup(strGroupName="EdgeGroup1", crlTargets=[Edge(122, 121)])
        Tools.Group.CreateGroup(strGroupName="PartGroup1", crlTargets=[Part(5)])
        Tools.Group.CreateGroup(strGroupName="Element2DGroup1", crlTargets=[Elem(3166, 2439, 2367)])
        Tools.Group.CreateGroup(strGroupName="NodeGroup1", crlTargets=[Node(1217, 977, 1116, 1286)])
        Home.Find(strSearch="1 2 3 4 5", strSelectedType="Group")
        JPT.ViewFitToModel()
        
        # Get the information of all selected groups
        listSelGroups = JPT.GetSelectedGroups()
        JPT.Debugger(listSelGroups)
        JPT.Debugger(listSelGroups[4])
        ```
        
        """
        message = "JPT.GetSelectedGroups({})".format('')
        return JPT_RUN_LINE(message)

    def GetSelectedGroupsCr():
        r"""
        ## Description
        
        Get all information of the selected groups under _List of Cursor_ format.
        
        ## Syntax
        
        ```psj
        JPT.GetSelectedGroupsCr()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _String_ specifying a cursor list (Macro string type) containing typeID and ID of the selected groups.
        
        ## Sample Code
        
        ```psj {18}
        # Prepare model
        Geometry.Part.Cube(iPartColor=7138156)
        Geometry.Part.Cube(strName="Cube_2", iPartColor=5921475)
        Geometry.Part.Cube(strName="Cube_3", iPartColor=6678117)
        Geometry.Part.Cube(strName="Cube_4", iPartColor=11908427)
        Geometry.Part.Cube(strName="Cube_5", iPartColor=15429611)
        Geometry.Part.Cube(strName="Cube_6", iPartColor=7531634)
        Geometry.Part.Cube(strName="Cube_7", iPartColor=12434775)
        Tools.Group.CreateGroup(strGroupName="FaceGroup1", crlTargets=[Face(130)])
        Tools.Group.CreateGroup(strGroupName="EdgeGroup1", crlTargets=[Edge(122, 121)])
        Tools.Group.CreateGroup(strGroupName="PartGroup1", crlTargets=[Part(5)])
        Tools.Group.CreateGroup(strGroupName="Element2DGroup1", crlTargets=[Elem(3166, 2439, 2367)])
        Tools.Group.CreateGroup(strGroupName="NodeGroup1", crlTargets=[Node(1217, 977, 1116, 1286)])
        Home.Find(strSearch="1 2 3 4 5", strSelectedType="Group")
        JPT.ViewFitToModel()
        
        # Get the information of all selected groups
        listCursorSelGroups = JPT.GetSelectedGroupsCr()
        JPT.Debugger(listCursorSelGroups)
        ```
        
        """
        message = "JPT.GetSelectedGroupsCr({})".format('')
        return JPT_RUN_LINE(message)

    def GetSelectedNodes():
        r"""
        ## Description
        
        Get all information of the selected nodes.
        
        ## Syntax
        
        ```psj
        JPT.GetSelectedNodes()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[NodeVector](../data-type/psj-utility/pre-utility/built-in-types/NodeVector)_ object or _List of [DNode](../data-type/psj-utility/pre-utility/built-in-types/DNode)_ objects containing all the information of the selected nodes.
        
        ## Sample Code
        
        ```psj {13}
        # Prepare model
        Geometry.Part.Cube(iPartColor=7138156)
        Geometry.Part.Cube(strName="Cube_2", iPartColor=5921475)
        Geometry.Part.Cube(strName="Cube_3", iPartColor=6678117)
        Geometry.Part.Cube(strName="Cube_4", iPartColor=11908427)
        Geometry.Part.Cube(strName="Cube_5", iPartColor=15429611)
        Geometry.Part.Cube(strName="Cube_6", iPartColor=7531634)
        Geometry.Part.Cube(strName="Cube_7", iPartColor=12434775)
        Home.Find(strSearch="20 21 22 23 24", strSelectedType="Node")
        JPT.ViewFitToModel()
        
        # Get the information of all selected nodes
        listSelNodes = JPT.GetSelectedNodes()
        JPT.Debugger(listSelNodes)
        JPT.Debugger(listSelNodes[1])
        ```
        
        """
        message = "JPT.GetSelectedNodes({})".format('')
        return JPT_RUN_LINE(message)

    def GetSelectedNodesCr():
        r"""
        ## Description
        
        Get all information of the selected nodes under _List of Cursor_ format.
        
        ## Syntax
        
        ```psj
        JPT.GetSelectedNodesCr()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _String_ specifying a cursor list (Macro string type) containing typeID and ID of the selected nodes.
        
        ## Sample Code
        
        ```psj {13}
        # Prepare model
        Geometry.Part.Cube(iPartColor=7138156)
        Geometry.Part.Cube(strName="Cube_2", iPartColor=5921475)
        Geometry.Part.Cube(strName="Cube_3", iPartColor=6678117)
        Geometry.Part.Cube(strName="Cube_4", iPartColor=11908427)
        Geometry.Part.Cube(strName="Cube_5", iPartColor=15429611)
        Geometry.Part.Cube(strName="Cube_6", iPartColor=7531634)
        Geometry.Part.Cube(strName="Cube_7", iPartColor=12434775)
        Home.Find(strSearch="20 21 22 23 24", strSelectedType="Node")
        JPT.ViewFitToModel()
        
        # Get the information of all selected nodes
        listCursorSelNodes = JPT.GetSelectedNodesCr()
        JPT.Debugger(listCursorSelNodes)
        ```
        
        """
        message = "JPT.GetSelectedNodesCr({})".format('')
        return JPT_RUN_LINE(message)

    def GetSelectedParts():
        r"""
        ## Description
        
        Get all information of the selected parts.
        
        ## Syntax
        
        ```psj
        JPT.GetSelectedParts()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[BodyVector](../data-type/psj-utility/pre-utility/built-in-types/BodyVector)_ object or _List of [DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_ objects containing all the information of the selected parts.
        
        ## Sample Code
        
        ```psj {13}
        # Prepare model
        Geometry.Part.Cube(iPartColor=7138156)
        Geometry.Part.Cube(strName="Cube_2", iPartColor=5921475)
        Geometry.Part.Cube(strName="Cube_3", iPartColor=6678117)
        Geometry.Part.Cube(strName="Cube_4", iPartColor=11908427)
        Geometry.Part.Cube(strName="Cube_5", iPartColor=15429611)
        Geometry.Part.Cube(strName="Cube_6", iPartColor=7531634)
        Geometry.Part.Cube(strName="Cube_7", iPartColor=12434775)
        Home.Find(strSearch="5 6 7 8", strSelectedType="Part")
        JPT.ViewFitToModel()
        
        # Get the information of all selected parts
        listSelParts = JPT.GetSelectedParts()
        JPT.Debugger(listSelParts)
        JPT.Debugger(listSelParts[2])
        ```
        
        """
        message = "JPT.GetSelectedParts({})".format('')
        return JPT_RUN_LINE(message)

    def GetSelectedPartsCr():
        r"""
        ## Description
        
        Get all information of the selected parts under _List of Cursor_ format.
        
        ## Syntax
        
        ```psj
        JPT.GetSelectedPartsCr()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _String_ specifying a cursor list (Macro string type) containing typeID and ID of the selected parts.
        
        ## Sample Code
        
        ```psj {13}
        # Prepare model
        Geometry.Part.Cube(iPartColor=7138156)
        Geometry.Part.Cube(strName="Cube_2", iPartColor=5921475)
        Geometry.Part.Cube(strName="Cube_3", iPartColor=6678117)
        Geometry.Part.Cube(strName="Cube_4", iPartColor=11908427)
        Geometry.Part.Cube(strName="Cube_5", iPartColor=15429611)
        Geometry.Part.Cube(strName="Cube_6", iPartColor=7531634)
        Geometry.Part.Cube(strName="Cube_7", iPartColor=12434775)
        Home.Find(strSearch="5 6 7", strSelectedType="Part")
        JPT.ViewFitToModel()
        
        # Get the information of all selected parts
        listCursorSelParts = JPT.GetSelectedPartsCr()
        JPT.Debugger(listCursorSelParts)
        ```
        
        """
        message = "JPT.GetSelectedPartsCr({})".format('')
        return JPT_RUN_LINE(message)

    def GetSharedElements(DItemVector):
        r"""
        ## Description
        
        Get all information of the shared elements.
        
        ## Syntax
        
        ```psj
        JPT.GetSharedElements(DItemVector)
        ```
        
        ## Inputs
        
        ### `DItemVector`
        
        - A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects to get the shared elements.
        - This is a required input.
        
        ## Return Code
        
        A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing all the information of all the shared elements.
        
        ## Sample Code
        
        ```psj {14}
        # Prepare model
        Geometry.Part.Cube(iPartColor=6217822)
        Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6908379)
        Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=7138924)
        Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube_4", iPartColor=15753968)
        JPT.ViewFitToModel()
        
        # Create shared faces
        JPT.Exec('AssembleFaceMatingStep([], [], [3:1, 3:2, 3:3, 3:4], 1e-05)')
        JPT.Exec('AssembleFaceEx([49, 24, 50, 75, 101, 76], 1e-05, 0, 0)')
        
        # Get the information of all shared elements
        listParts = JPT.GetAllByTypeID(JPT.DItemType.BODY)
        listSharedElems = JPT.GetSharedElements(listParts)
        JPT.Debugger(listSharedElems)
        ```
        
        """
        message = "JPT.GetSharedElements({})".format(DItemVector)
        return JPT_RUN_LINE(message)

    def GetSharedFaces(DItemVector):
        r"""
        ## Description
        
        Get all information of the shared faces.
        
        ## Syntax
        
        ```psj
        JPT.GetSharedFaces(DItemVector)
        ```
        
        ## Inputs
        
        ### `DItemVector`
        
        - A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects to get the shared faces.
        - This is a required input.
        
        ## Return Code
        
        A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing all the information of all the shared faces.
        
        ## Sample Code
        
        ```psj {14}
        # Prepare model
        Geometry.Part.Cube(iPartColor=6217822)
        Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6908379)
        Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=7138924)
        Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube_4", iPartColor=15753968)
        JPT.ViewFitToModel()
        
        # Create shared faces
        JPT.Exec('AssembleFaceMatingStep([], [], [3:1, 3:2, 3:3, 3:4], 1e-05)')
        JPT.Exec('AssembleFaceEx([49, 24, 50, 75, 101, 76], 1e-05, 0, 0)')
        
        # Get the information of all shared faces
        listParts = JPT.GetAllByTypeID(JPT.DItemType.BODY)
        listSharedFaces = JPT.GetSharedFaces(listParts)
        JPT.Debugger(listSharedFaces)
        ```
        
        """
        message = "JPT.GetSharedFaces({})".format(DItemVector)
        return JPT_RUN_LINE(message)

    def GetSharedNodes(DItemVector):
        r"""
        ## Description
        
        Get all information of the shared nodes.
        
        ## Syntax
        
        ```psj
        JPT.GetSharedNodes(DItemVector)
        ```
        
        ## Inputs
        
        ### `DItemVector`
        
        - A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects to get the shared nodes.
        - This is a required input.
        
        ## Return Code
        
        A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects containing all the information of all the shared nodes.
        
        ## Sample Code
        
        ```psj {14}
        # Prepare model
        Geometry.Part.Cube(iPartColor=6217822)
        Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6908379)
        Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=7138924)
        Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube_4", iPartColor=15753968)
        JPT.ViewFitToModel()
        
        # Create shared faces
        JPT.Exec('AssembleFaceMatingStep([], [], [3:1, 3:2, 3:3, 3:4], 1e-05)')
        JPT.Exec('AssembleFaceEx([49, 24, 50, 75, 101, 76], 1e-05, 0, 0)')
        
        # Get the information of all shared nodes
        listParts = JPT.GetAllByTypeID(JPT.DItemType.BODY)
        listSharedNodes = JPT.GetSharedNodes(listParts)
        JPT.Debugger(listSharedNodes)
        ```
        
        """
        message = "JPT.GetSharedNodes({})".format(DItemVector)
        return JPT_RUN_LINE(message)

    def GetSuppressedParts():
        r"""
        ## Description
        
        Get all information of all suppressed parts.
        
        ## Syntax
        
        ```psj
        JPT.GetSuppressedParts()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        A _[BodyVector](../data-type/psj-utility/pre-utility/built-in-types/BodyVector)_ object or _List of [DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_ objects containing all the information of the suppressed parts (parts which are suppressed/disabled in Assembly Tree and can not be accessed).
        
        ## Sample Code
        
        ```psj {13}
        # Prepare model
        Geometry.Part.Cube(iPartColor=7138156)
        Geometry.Part.Cube(strName="Cube_2", iPartColor=5921475)
        Geometry.Part.Cube(strName="Cube_3", iPartColor=6678117)
        Geometry.Part.Cube(strName="Cube_4", iPartColor=11908427)
        Geometry.Part.Cube(strName="Cube_5", iPartColor=15429611)
        Geometry.Part.Cube(strName="Cube_6", iPartColor=7531634)
        Geometry.Part.Cube(strName="Cube_7", iPartColor=12434775)
        Assembly.RightClick.Suppress(crlParts=[Part(3, 5, 4)])
        JPT.ViewFitToModel()
        
        # Get the information of all selected parts
        listSuppressedParts = JPT.GetSuppressedParts()
        JPT.Debugger(listSuppressedParts) #list has size = 3
        JPT.Debugger(listSuppressedParts[0]) #DBody item: Cube 3
        ```
        
        """
        message = "JPT.GetSuppressedParts({})".format('')
        return JPT_RUN_LINE(message)

    def GetThicknessOfEntity(DItemType, entityID):
        r"""
        ## Description
        
        Get thickness of the inputted entity ID (Available for Part/Face/Element only).
        
        ## Syntax
        
        ```psj
        JPT.GetThicknessOfEntity(DItemType, entityID)
        ```
        
        ## Inputs
        
        ### `DItemType`
        
        - An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.
        - This is a required input.
        
        ### `entityID`
        
        - An _Integer_ specifying the ID of Part/Face/Element.
        - This is a required input.
        
        ## Return Code
        
        A _Double_ specifying the thickness of the target entity.
        
        ## Sample Code
        
        ```psj {25-28}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(dlOrigin=[0.012, 0.0, 0.0], strName="Cube_2", iPartColor=6149981)
        Properties.Material.Add(strMaterialName="Structural_Steel", listMaterialProperty=[Density([(DENSITY, 7.85e-09)]),
            Elastic([(YOUNGS_MODULUS, 200000.0), (POISSONS_RATIO, 0.3)])])
        Properties.Shell(crlTargets=[Face(26)], strName="Shell Property 1", iPropertyColor=16131973,
            crMatMembrane=Material(1), crMatBend=Material(1), crMatShear=Material(1), dMatOrient1=DFLT_DBL,
            dThickness=0.005, dBendStiff=DFLT_DBL, dThickRatio=DFLT_DBL, dNSM=DFLT_DBL, dFiberDist1=DFLT_DBL,
            dFiberDist2=DFLT_DBL, dPlateOff=DFLT_DBL, iItgPts=DFLT_INT)
        Properties.Shell(crlTargets=[Face(52)], strName="Shell Property 2", iPropertyId=2, iPropertyColor=7010958,
            crMatMembrane=Material(1), crMatBend=Material(1), crMatShear=Material(1), dMatOrient1=DFLT_DBL,
            dThickness=0.01, dBendStiff=DFLT_DBL, dThickRatio=DFLT_DBL, dNSM=DFLT_DBL, dFiberDist1=DFLT_DBL,
            dFiberDist2=DFLT_DBL, dPlateOff=DFLT_DBL, iItgPts=DFLT_INT)
        Properties.Shell(crlTargets=[Face(22)], strName="Shell Property 3", iPropertyId=3, iPropertyColor=3962802,
            crMatMembrane=Material(1), crMatBend=Material(1), crMatShear=Material(1), dMatOrient1=DFLT_DBL,
            dThickness=0.015, dBendStiff=DFLT_DBL, dThickRatio=DFLT_DBL, dNSM=DFLT_DBL, dFiberDist1=DFLT_DBL,
            dFiberDist2=DFLT_DBL, dPlateOff=DFLT_DBL, iItgPts=DFLT_INT)
        Properties.Shell(crlTargets=[Face(48)], strName="Shell Property 4", iPropertyId=4, iPropertyColor=6396734,
            crMatMembrane=Material(1), crMatBend=Material(1), crMatShear=Material(1), dMatOrient1=DFLT_DBL,
            dThickness=0.02, dBendStiff=DFLT_DBL, dThickRatio=DFLT_DBL, dNSM=DFLT_DBL, dFiberDist1=DFLT_DBL,
            dFiberDist2=DFLT_DBL, dPlateOff=DFLT_DBL, iItgPts=DFLT_INT)
        JPT.ViewFitToModel()
        
        #Get all the existing connections
        dThickness_1 = JPT.GetThicknessOfEntity(JPT.DItemType.FACE,26)
        dThickness_2 = JPT.GetThicknessOfEntity(JPT.DItemType.FACE,52)
        dThickness_3 = JPT.GetThicknessOfEntity(JPT.DItemType.FACE,22)
        dThickness_4 = JPT.GetThicknessOfEntity(JPT.DItemType.FACE,48)
        JPT.Debugger(dThickness_1)
        JPT.Debugger(dThickness_2)
        JPT.Debugger(dThickness_3)
        JPT.Debugger(dThickness_4)
        ```
        
        """
        message = "JPT.GetThicknessOfEntity({},{})".format(DItemType,entityID)
        return JPT_RUN_LINE(message)

    def GetTimeStepInfoName(PostAnalysisType, resultSet, timeStep):
        r"""
        ## Description
        
        Get the name of Time Step Info.
        
        ## Syntax
        
        ```psj
        JPT.GetTimeStepInfoName(PostAnalysisType,
                                resultSet,
                                timeStep)
        ```
        
        ## Inputs
        
        ### `PostAnalysisType`
        
        - An _Enum_ specifying the _[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.
        - This is a required input.
        
        ### `resultSet`
        
        - An _Integer_ specifying the step ID of the imported result.
        - This is a required input.
        
        ### `timeStep`
        
        - An _Integer_ specifying the time step of the imported result.
        - This is a required input.
        
        ## Return Code
        
        A _String_ specifying the name of Time Step information.
        
        ## Sample Code
        
        ```psj {5}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        time_step_info_name = JPT.GetTimeStepInfoName(2,1,1)
        JPT.Debugger(time_step_info_name) # Mode 1, Freq=3.235953e+04
        ```
        
        """
        message = "JPT.GetTimeStepInfoName({},{},{})".format(PostAnalysisType,resultSet,timeStep)
        return JPT_RUN_LINE(message)

    def GetUndoCount():
        r"""
        ## Description
        
        Get the total number of undo action which is capable of executing.
        
        ## Syntax
        
        ```psj
        JPT.GetUndoCount()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        An _Integer_ specifying the number of Undo operation.
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model and undo steps
        Geometry.Part.Cube(strName="Cube_11", iPartColor=11842649)
        Geometry.Part.Cube(strName="Cube_12", iPartColor=14968422)
        Geometry.Part.Cube(strName="Cube_13", iPartColor=6250447)
        Geometry.Part.Cube(strName="Cube_14", iPartColor=12734402)
        Geometry.Part.Cube(strName="Cube_15", iPartColor=16579696)
        Geometry.Part.Cube(strName="Cube_16", iPartColor=7666683)
        Geometry.Part.Cube(strName="Cube_17", iPartColor=12867524)
        
        # Get the number of the available Undo
        iUndoSteps = JPT.GetUndoCount()
        JPT.Debugger(iUndoSteps) # Return an integer object with value = 7
        ```
        
        """
        message = "JPT.GetUndoCount({})".format('')
        return JPT_RUN_LINE(message)

    def HidePreview():
        r"""
        ## Description
        
        Hide preview render on the main screen. Preview is still existing, but it will be hidden.
        
        ## Syntax
        
        ```psj
        JPT.HidePreview(...)
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {12}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], strName="Cube_2", iPartColor=13259210)
        JPT.ViewFitToModel()
        
        #Preview:
        color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
        parts = JPT.GetAllParts()
        JPT.PreviewScaling(parts,[2,1.1,1.1],[0,0,0],color,0.2)
        
        #Hide Preview:
        JPT.HidePreview()
        ```
        
        """
        message = "JPT.HidePreview({})".format('')
        return JPT_RUN_LINE(message)

    def HighlightByID(DItemType, entityID, BoolType):
        r"""
        ## Description
        
        Highlight an item in Assembly tree by using its _[DItemType](../data-type/psj-command/DItem-types)_ and its ID.
        
        ## Syntax
        
        ```psj
        JPT.HighlightByID(DItemType, entityID, BoolType)
        ```
        
        ## Inputs
        
        ### `DItemType`
        
        - An _Enum_ specifying _[DItemType](../data-type/psj-command/DItem-types)_ of the target entities.
        - This is a required input.
        
        ### `entityID`
        
        - An _Integer_ specifying ID of the selecting entity.
        - This is a required input.
        
        ### `BoolType`
        
        - An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the selection mode:
          - _True_: Select the inputted entity with its ID.
          - _False_: Deselect the inputted entity with its ID.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {18}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
        Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=13259210)
        JPT.ViewFitToModel()
        
        # Create LBCs
        BoundaryConditions.Pressure.General(dPressure=100000000.0, crlTargets=[Face(26)])
        BoundaryConditions.Force.General(forceLBC=FORCE_LBC(vecForce=[DFLT_DBL, DFLT_DBL, -10.0]), 
            crlTargets=[Face(52)])
        BoundaryConditions.FixedConstraint(crlTargets=[Face(77, 51, 25)])
        
        # Highlight Pressure item in Assembly tree
        listDItemLoadBCs = JPT.GetAllLoadsBCs()
        for lbc in listDItemLoadBCs:
            if lbc.type == JPT.DItemType.LBC_G_PRESSURE:
                iID = lbc.id
        JPT.HighlightByID(JPT.DItemType.LBC_G_PRESSURE, iID, JPT.BoolType.TRUE_VAL)
        ```
        
        """
        message = "JPT.HighlightByID({},{},{})".format(DItemType,entityID,BoolType)
        return JPT_RUN_LINE(message)

    def InverseHideBodies(partID):
        r"""
        ## Description
        
        Show the part having the inputted ID only.
        
        ## Syntax
        
        ```psj
        JPT.InverseHideBodies(partID)
        ```
        
        ## Inputs
        
        ### `partID`
        
        - An _Integer_ specifying the ID of the part which will be shown only.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {12}
        # Prepare model
        Geometry.Part.Cube(strName="Cube_11", iPartColor=11842649)
        Geometry.Part.Cube(strName="Cube_12", iPartColor=14968422)
        Geometry.Part.Cube(strName="Cube_13", iPartColor=6250447)
        Geometry.Part.Cube(strName="Cube_14", iPartColor=12734402)
        Geometry.Part.Cube(strName="Cube_15", iPartColor=16579696)
        
        # Show the part with ID = 3 only (Cube_13)
        selAllParts = JPT.GetAllParts()
        showPart = selAllParts[2].id
        JPT.Debugger(selAllParts[2])
        JPT.InverseHideBodies(showPart)
        ```
        
        """
        message = "JPT.InverseHideBodies({})".format(partID)
        return JPT_RUN_LINE(message)

    def IsSpatialPointRendered(posX, posY, posZ):
        r"""
        ## Description
        
        Check if a specified point (node) that has the spatial coordinates (X, Y, Z) is rendered in the current view.
        
        ## Syntax
        
        ```psj
        JPT.IsSpatialPointRendered(posX, posY, posZ)
        ```
        
        ## Inputs
        
        ### `posX`
        
        - A _Double_ specifying the X coordinate of the specified point (node).
        - This is a required input.
        
        ### `posY`
        
        - A _Double_ specifying the Y coordinate of the specified point (node).
        - This is a required input.
        
        ### `posZ`
        
        - A _Double_ specifying the Z coordinate of the specified point (node).
        - This is a required input.
        
        ## Return Code
        
        A _Boolean_ specifying the status of the specified point (node):
        - _True_: The specified point (node) can be rendered.
        - _False_: The specified point (node) is hidden.
        
        ## Sample Code
        
        ```psj {10}
        # Prepare model
        Geometry.Part.Cube(iPartColor=6974164)
        JPT.ViewFitToModel()
        
        # Select a node with ID = 7
        JPT.SelectionByID(JPT.DItemType.NODE, 7, True)
        listSelNodes = JPT.GetSelectedNodes()
        
        # Check if the selected node is rendered
        result=JPT.IsSpatialPointRendered(listSelNodes[0].pos.x, listSelNodes[0].pos.y, listSelNodes[0].pos.z)
        print(result)
        ```
        
        """
        message = "JPT.IsSpatialPointRendered({},{},{})".format(posX,posY,posZ)
        return JPT_RUN_LINE(message)

    def ListDoubleToMacroVector(doubleValue1, doubleValue2, doubleValue3):
        r"""
        ## Description
        
        Convert a _List_ of 3 _Double_ values to a Vector3D (Macro string type).
        
        ## Syntax
        
        ```psj
        JPT.ListDoubleToMacroVector(doubleValue1, doubleValue2, doubleValue3)
        ```
        
        ## Inputs
        
        ### `doubleValue1`
        
        - A _Double_ specifying the first value which will be used for converting.
        - This is a required input.
        
        ### `doubleValue2`
        
        - A _Double_ specifying the second value which will be used for converting.
        - This is a required input.
        
        ### `doubleValue3`
        
        - A _Double_ specifying the third value which will be used for converting.
        - This is a required input.
        
        ## Return Code
        
        A _String_ specifying the converted Vector3D (Macro string type).
        
        ## Sample Code
        
        ```psj {6}
        # Convert a list of 3 double values to a vector3d (Macro string type)
        inputValue1 = 0.001
        inputValue2 = 2.1
        inputValue3 = 5.5
        # Return a string object with value = [0.001,2.1,5.5]
        JPT.Debugger(JPT.ListDoubleToMacroVector(inputValue1, inputValue2, inputValue3))
        ```
        
        """
        message = "JPT.ListDoubleToMacroVector({},{},{})".format(doubleValue1,doubleValue2,doubleValue3)
        return JPT_RUN_LINE(message)

    def MacroListTCursorToListDItem(cursorList):
        r"""
        ## Description
        
        Convert a cursor list (Macro string type) to a _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_.
        
        ## Syntax
        
        ```psj
        JPT.MacroListTCursorToListDItem(cursorList)
        ```
        
        ## Inputs
        
        ### `cursorList`
        
        - A _String_ specifying the cursor list (Macro string type).
        - This is a required input.
        
        ## Return Code
        
        A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List_ of _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects specifying the converted items.
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model
        Geometry.Part.Cube()
        
        # Convert a cursor list (Macro string type) to a DItemVector
        ## Create a list of Node cursor
        strCursorNode1 = "10:467"
        strCursorNode2 = "10:477"
        strCursorNode3 = "10:483"
        listCursorNode = f"[{strCursorNode1}, {strCursorNode2}, {strCursorNode3}]"
        ## Convert cursor list to list of DItem
        JPT.Debugger(JPT.MacroListTCursorToListDItem(listCursorNode))
        ```
        
        """
        message = "JPT.MacroListTCursorToListDItem({})".format(cursorList)
        return JPT_RUN_LINE(message)

    def MacroResultParser(returnedMacroString, listOfStringPattern):
        r"""
        ## Description
        
        Splitting the returned value from an executed macro to a _List of Strings_.
        
        ## Syntax
        
        ```psj
        JPT.MacroResultParser(returnedMacroString, listOfStringPattern)
        ```
        
        ## Inputs
        
        ### `returnedMacroString`
        
        - A _String_ specifying the returned value from the executed macro.
        - This is a required input.
        
        ### `listOfStringPattern`
        
        - A _List of String_ pattern splitting from the returned MacroString.
          - The output list requiring the below values:
            - string
            - cursor
            - cursor_pair
            - list_number
            - list_cursor_pair
            - list_cursor
            - list_list_cursor
            - list_string
            - vector3d
            - number
        - This is a required input.
        
        ## Return Code
        
        A _List_ split from the returned value from an executed macro containing strings.
        
        ## Sample Code
        
        ```psj {45}
        '''
        Structure: JPT.MacroResultParser(input_string, arg_pattern)
        
        Supporting type for arg_pattern:
        "string",
        "cursor",
        "cursor_pair",
        "list_cursor_pair",
        "list_cursor",
        "list_list_cursor",
        "list_string",
        "vector3d",
        "list_number",
        "number"
        '''
        
        print(__doc__)
        
        import re
        
        Geometry.Part.Cube()
        Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
        Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_3", iPartColor=7697908)
        Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0], strName="Cube_4", iPartColor=7463537)
        Geometry.Part.Cube(dlOrigin=[0.03, 0.01, 0.0], strName="Cube_5", iPartColor=7434735)
        Geometry.Part.Cube(dlOrigin=[0.03, 0.02, 0.0], strName="Cube_6", iPartColor=14903267)
        Geometry.Part.Cube(dlOrigin=[0.03, 0.03, 0.0], strName="Cube_7", iPartColor=15658599)
        Geometry.Part.Cube(dlOrigin=[0.02, 0.03, 0.0], strName="Cube_8", iPartColor=7961077)
        Geometry.Part.Cube(dlOrigin=[0.01, 0.03, 0.0], strName="Cube_9", iPartColor=7829501)
        Geometry.Part.Cube(dlOrigin=[0.0, 0.03, 0.0], strName="Cube_10", iPartColor=11842649)
        Geometry.Part.Cube(dlOrigin=[0.0, 0.02, 0.0], strName="Cube_11", iPartColor=14968422)
        Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], strName="Cube_12", iPartColor=6250447)
        Geometry.Part.Cube(dlOrigin=[0.01, 0.01, 0.0], strName="Cube_13", iPartColor=12734402)
        Geometry.Part.Cube(dlOrigin=[0.02, 0.01, 0.0], strName="Cube_14", iPartColor=16579696)
        Geometry.Part.Cube(dlOrigin=[0.02, 0.02, 0.0], strName="Cube_15", iPartColor=7666683)
        Geometry.Part.Cube(dlOrigin=[0.01, 0.02, 0.0], strName="Cube_18", iPartColor=13787489)
        
        select_contact_face = JPT.Exec('FindContactPairsDynamic([{}], 0, 0, 0.001, 1, 1, 0.001)'.\
                                    format(", ".join([("3:" + str(_.id)) for _ in JPT.GetAllParts()])))
        
        arg_pattern = ["number",
                       "list_string",
                       "list_list_cursor",
                       "list_list_cursor"]
        list_args = JPT.MacroResultParser(select_contact_face, arg_pattern)
        JPT.Debugger(list_args)
        
        print(
            f"Finding status : \
                {'Found contacts' if list_args[1]!=[] and list_args[1]!=[] else 'This model does not have contact'}"
        )
        
        number_of_matching = len((re.sub("\]|\[", "", list_args[1]).strip().split(",")))
        print(f"Number of contacts: {number_of_matching}")
        
        JPT.Exec('FindContact({0}, {1}, {2}, [{3}], [{4}], [{5}], [{6}], [{7}], \
                              [{8}], [{9}], [{10}])'.\
                  format(list_args[1],
                         list_args[2],
                         list_args[3],
                         ",".join(["1" for _ in range(number_of_matching)]),
                         ",".join(["0.001" for _ in range(number_of_matching)]),
                         ",".join(["1.79769e+308" for _ in range(number_of_matching)]),
                         ",".join(["0" for _ in range(number_of_matching)]),
                         ",".join(["65280" for _ in range(number_of_matching)]),
                         ",".join(["0:0" for _ in range(number_of_matching)]),
                         ",".join(["0:0" for _ in range(number_of_matching)]),
                         ",".join(["0:0" for _ in range(number_of_matching)])))
        ```
        
        """
        message = "JPT.MacroResultParser({},{})".format(returnedMacroString,listOfStringPattern)
        return JPT_RUN_LINE(message)

    def MacroTCursorPairToDItemPair(cursorPair):
        r"""
        ## Description
        
        Convert cursor pair (Macro string type) to a pair of _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object.
        
        ## Syntax
        
        ```psj
        JPT.MacroTCursorPairToDItemPair(cursorPair)
        ```
        
        ## Inputs
        
        ### `cursorPair`
        
        - A _String_ specifying the cursor pair (Macro string type).
        - This is a required input.
        
        ## Return Code
        
        A _[DItemPair](../data-type/psj-utility/pre-utility/built-in-types/DItemPair)_ object.
        
        ## Sample Code
        
        ```psj {7}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=7730934)
        JPT.ViewFitToModel()
        
        # Get all the information of the 2 created cubes
        dItemPair = JPT.Debugger(JPT.MacroTCursorPairToDItemPair("3:1-3:2"))
        JPT.Debugger(dItemPair.firstDItem)
        JPT.Debugger(dItemPair.secondDItem)
        ```
        
        """
        message = "JPT.MacroTCursorPairToDItemPair({})".format(cursorPair)
        return JPT_RUN_LINE(message)

    def MacroTCursorToDItem(cursor):
        r"""
        ## Description
        
        Convert cursor (Macro string type) to a _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object.
        
        ## Syntax
        
        ```psj
        JPT.MacroTCursorToDItem(cursor)
        ```
        
        ## Inputs
        
        ### `cursor`
        
        - A _String_ specifying the cursor (Macro string type).
        - This is a required input.
        
        ## Return Code
        
        A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object.
        
        ## Sample Code
        
        ```psj {6}
        # Prepare model
        Geometry.Part.Cube()
        JPT.ViewFitToModel()
        
        # Convert to DItem and get all the information of the created Cube_1
        dItem = JPT.Debugger(JPT.MacroTCursorToDItem("3:1"))
        JPT.Debugger(dItem)
        ```
        
        """
        message = "JPT.MacroTCursorToDItem({})".format(cursor)
        return JPT_RUN_LINE(message)

    def MessageBoxPSJ(messageContent, messageBoxType):
        r"""
        ## Description
        
        Show a Jupiter dialog (Information, Warning).
        
        ## Syntax
        
        ```psj
        JPT.MessageBoxPSJ(messageContent, messageBoxType)
        ```
        
        ## Inputs
        
        ### `messageContent`
        
        - A _String_ specifying the message which will be shown on the created message box.
        - This is a required input.
        
        ### `messageBoxType`
        
        - An _Enum_ specifying the _[MsgBoxType](../data-type/psj-utility/pre-utility/enumeration-types/msgbox-types)_ describing the type of creating message box in Jupiter.
        - This is a required input.
        
        ## Return Code
        
        The selected option (YES, NO, OK, CANCEL).
        
        ## Sample Code
        
        ```psj {2}
        # Show an information message box
        returnValue = JPT.MessageBoxPSJ("Test dialog",JPT.MsgBoxType.MB_INFORMATION_OK)
        JPT.Debugger(returnValue) # Return a string object with value = OK
        ```
        
        """
        message = "JPT.MessageBoxPSJ({},{})".format(messageContent,messageBoxType)
        return JPT_RUN_LINE(message)

    def MsgOut(outputString):
        r"""
        ## Description
        
        Print a text to the Jupiter API window.
        
        ## Syntax
        
        ```psj
        JPT.MsgOut(outputString)
        ```
        
        ## Inputs
        
        ### `outputString`
        
        - A _String_ specifying the content which will be printed out to the Jupiter API window.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {2}
        # Print the bellow text to the Jupiter API window
        JPT.MsgOut('print a text') # print a text
        ```
        
        """
        message = "JPT.MsgOut({})".format(outputString)
        return JPT_RUN_LINE(message)

    def PostHasDeform(PostAnalysisType, resultSet, timeStep):
        r"""
        ## Description
        
        Check whether the working result has deformation or not.
        
        ## Syntax
        
        ```psj
        JPT.PostHasDeform(PostAnalysisType,
                          resultSet,
                          timeStep)
        ```
        
        ## Inputs
        
        ### `PostAnalysisType`
        
        - An _Enum_ specifying the _[PostAnalysisType](../data-type/psj-utility/post-utility/enumeration-types/post-analysis-types)_ describing the type of analysis result.
        - This is a required input.
        
        ### `resultSet`
        
        - An _Integer_ specifying the step ID of the imported result.
        - This is a required input.
        
        ### `timeStep`
        
        - An _Integer_ specifying the time step of the imported result.
        - This is a required input.
        
        ## Return Code
        
        A _Boolean_ specifying the working result has deformation or not.
        
        ## Sample Code
        
        ```psj {10}
        # Prepare model
        samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
        JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))
        
        JPT.Exec('CmdShowPostContour(183:1, {1, 0, 1, 1, Stress, XY, 4}, {1, 1, 0, 0, 1, 8, \
                                     0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, \
                                     {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, {0, 0, 0, 0, , , 0}, \
                                     {0, 0, 0, 0, 0, 0, 0, 0.000000, 0}, 0, 0)')
        
        bool_check_deform = JPT.PostHasDeform(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC, 1, 1)
        JPT.Debugger(bool_check_deform) #True
        ```
        
        """
        message = "JPT.PostHasDeform({},{},{})".format(PostAnalysisType,resultSet,timeStep)
        return JPT_RUN_LINE(message)

    def PreviewBCForceGeneral(DItemVector, dlForce, dlMoment, iArrowDir=0, iColor=255, dTransparency=0.5):
        r"""
        ## Description
        
        Show preview result of applying general force on target.
        
        ## Syntax
        
        ```psj
        JPT.PreviewBCForceGeneral(...)
        ```
        
        ## Inputs
        
        ### `DItemVector`
        
        - A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects storing the information of targets for applying force.
        - This targets can be Face, Edge or Node.
        - This is a required input.
        
        ### `dlForce`
        
        - A _List of Double_ specifying value of Force in 3 directions.
        - This is a required input.
        
        ### `dlMoment`
        
        - A _List of Double_ specifying value of Moment in 3 directions.
        - This is a required input.
        
        ### `iArrowDir`
        
        - An _Integer_ specifying the display arrow direction.
          - 0: Start at node.
          - 1: End at node.
        - The default value is 0.
        
        ### `iColor`
        
        - An _Integer_ specifying the color of the previewed entity.
        - The default value is 255.
        
        ### `dTransparency`
        
        - A _Double_ specifying the transparency of the previewed entity.
        - The range of `dTransparency` = [0.0, 1.0]
        - The default value is 0.5.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {10}
        # Clear Preview
        JPT.ClearPreview()
        
        # Prepare model
        Geometry.Part.Cube()
        
        # Preview
        color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
        selFace = JPT.GetEntitiesByID(JPT.DItemType.FACE, 26)
        JPT.PreviewBCForceGeneral(selFace,[0.0,10.0,10.0],[0.0,0.0,0.0],0,color,0.8)
        JPT.ViewFitToModel()
        ```
        
        """
        message = "JPT.PreviewBCForceGeneral({},{},{},{},{},{})".format(DItemVector,dlForce,dlMoment,iArrowDir,iColor,dTransparency)
        return JPT_RUN_LINE(message)

    def PreviewBCForceNormal(DElemForNormal, DItemVector, iArrowDir=0, iColor=255, dTransparency=0.5):
        r"""
        ## Description
        
        Show preview result of applying normal force on target.
        
        ## Syntax
        
        ```psj
        JPT.PreviewBCForceNormal(...)
        ```
        
        ## Inputs
        
        ### `DElemForNormal`
        
        - A _[DElem](../data-type/psj-utility/pre-utility/built-in-types/DElem)_ object specifying 2D element information.
        - This element will be used to calculate normal vector for force direction.
        - This is a required input.
        
        ### `DItemVector`
        
        - A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects storing the information of targets for applying force.
        - This targets can be Face, Edge or Node.
        - This is a required input.
        
        ### `iArrowDir`
        
        - An _Integer_ specifying the display arrow direction.
          - 0: Start at node.
          - 1: End at node.
        - The default value is 0.
        
        ### `iColor`
        
        - An _Integer_ specifying the color of the previewed entity.
        - The default value is 255.
        
        ### `dTransparency`
        
        - A _Double_ specifying the transparency of the previewed entity.
        - The range of `dTransparency` = [0.0, 1.0]
        - The default value is 0.5.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {12}
        # Clear Preview
        JPT.ClearPreview()
        
        # Prepare model
        Geometry.Part.Cube()
        
        # Preview
        color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
        selFace = JPT.GetEntitiesByID(JPT.DItemType.FACE, 26)
        normalElem = JPT.GetEntitiesByID(JPT.DItemType.ELEM, 1065)
        normalElem = JPT.CastDItemToDElem(normalElem[0])
        JPT.PreviewBCForceNormal(normalElem,selFace,0,color,0.8)
        JPT.ViewFitToModel()
        ```
        
        """
        message = "JPT.PreviewBCForceNormal({},{},{},{},{})".format(DElemForNormal,DItemVector,iArrowDir,iColor,dTransparency)
        return JPT_RUN_LINE(message)

    def PreviewBCPressureGeneral(DItemVector, iArrowDir=0, iColor=255, dTransparency=0.5):
        r"""
        ## Description
        
        Show preview result of applying general pressure on target.
        
        ## Syntax
        
        ```psj
        JPT.PreviewBCPressureGeneral(...)
        ```
        
        ## Inputs
        
        ### `DItemVector`
        
        - A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object or _List of [DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ objects storing the information of targets for applying pressure.
        - This targets can be Face, Edge or Node.
        - This is a required input.
        
        ### `iArrowDir`
        
        - An _Integer_ specifying the display arrow direction.
          - 0: Start at node.
          - 1: End at node.
        - The default value is 0.
        
        ### `iColor`
        
        - An _Integer_ specifying the color of the previewed entity.
        - The default value is 255.
        
        ### `dTransparency`
        
        - A _Double_ specifying the transparency of the previewed entity.
        - The range of `dTransparency` = [0.0, 1.0]
        - The default value is 0.5.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {10}
        # Clear Preview
        JPT.ClearPreview()
        
        # Prepare model
        Geometry.Part.Cube()
        
        # Preview
        color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
        selFace = JPT.GetEntitiesByID(JPT.DItemType.FACE, 26)
        JPT.PreviewBCPressureGeneral(selFace,1,color,0.8)
        JPT.ViewFitToModel()
        ```
        
        """
        message = "JPT.PreviewBCPressureGeneral({},{},{},{})".format(DItemVector,iArrowDir,iColor,dTransparency)
        return JPT_RUN_LINE(message)

    def PreviewMirror(DBodyVector, veclPoint, dOffset, iColor=255, dTransparency=0.5):
        r"""
        ## Description
        
        Show preview result of body mirror.
        
        ## Syntax
        
        ```psj
        JPT.PreviewMirror(...)
        ```
        
        ## Inputs
        
        ### `DBodyVector`
        
        - A _[DBodyVector](../data-type/psj-utility/pre-utility/built-in-types/BodyVector)_ object or _List of [DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_ objects storing the information of parts to be mirrored.
        - This is a required input.
        
        ### `veclPoint`
        
        - A _List of [TVector3D](../data-type/psj-utility/pre-utility/built-in-types/TVector3d)_ object specifying 3 node’s position to form a mirror plane.
        - This is a required input.
        
        ### `dOffset`
        
        - A _Double_ specifying the offset value.
        - This is a required input.
        
        ### `iColor`
        
        - An _Integer_ specifying the color of the previewed entity.
        - The default value is 255.
        
        ### `dTransparency`
        
        - A _Double_ specifying the transparency of the previewed entity.
        - The range of `dTransparency` = [0.0, 1.0]
        - The default value is 0.5.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {11}
        # Clear Preview
        JPT.ClearPreview()
        
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=13259210)
        
        # Preview
        color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
        parts = JPT.GetAllParts()
        JPT.PreviewMirror(parts,[[0.0055,0.01,0.0055],[0.005,0.01,0.0044],[0.0044,0.01,0.0044]],0,color,0.8)
        JPT.ViewFitToModel()
        ```
        
        """
        message = "JPT.PreviewMirror({},{},{},{},{})".format(DBodyVector,veclPoint,dOffset,iColor,dTransparency)
        return JPT_RUN_LINE(message)

    def PreviewRotate(DBodyVector, posCenter, vecAxis, dAngle, iColor=255, dTransparency=0.5, DCoord=None):
        r"""
        ## Description
        
        Show preview result of body rotation.
        
        ## Syntax
        
        ```psj
        JPT.PreviewRotate(...)
        ```
        
        ## Inputs
        
        ### `DBodyVector`
        
        - A _[DBodyVector](../data-type/psj-utility/pre-utility/built-in-types/BodyVector)_ object or _List of [DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_ objects storing the information of parts to be rotated.
        - This is a required input.
        
        ### `posCenter`
        
        - A _List_ specifying the center position of rotation.
        - This is a required input.
        
        ### `vecAxis`
        
        - A _List_ specifying the axis of rotation.
        - This is a required input.
        
        ### `dAngle`
        
        - A _Double_ specifying the rotation angle in degree.
        - This is a required input.
        
        ### `iColor`
        
        - An _Integer_ specifying the color of the previewed entity.
        - The default value is 255.
        
        ### `dTransparency`
        
        - A _Double_ specifying the transparency of the previewed entity.
        - The range of `dTransparency` = [0.0, 1.0]
        - The default value is 0.5.
        
        ### `DCoord`
        
        - A _[DCoord](../data-type/psj-utility/pre-utility/built-in-types/DCoord)_ object specifying Local Coordinate System.
        - The default value is None (Global Coordinate System).
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {13}
        # Clear Preview
        JPT.ClearPreview()
        
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], strName="Cube_2", iPartColor=13259210)
        Tools.Coordinates.ThreeNode(iOrder=-1, crlNodes=[Node(496, 578, 590)])
        
        # Preview
        color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
        parts = JPT.GetAllParts()
        coord = JPT.GetAllCoordinates()
        JPT.PreviewRotate(parts,[0,0,0],[0,1,0],45,color,0.8,coord[0])
        JPT.ViewFitToModel()
        ```
        
        """
        message = "JPT.PreviewRotate({},{},{},{},{},{},{})".format(DBodyVector,posCenter,vecAxis,dAngle,iColor,dTransparency,DCoord)
        return JPT_RUN_LINE(message)

    def PreviewScaling(DBodyVector, dlScaleVector, dlScaleCenter, iColor=255, dTransparency=0.5):
        r"""
        ## Description
        
        Show preview result of body scaling.
        
        ## Syntax
        
        ```psj
        JPT.PreviewScaling(...)
        ```
        
        ## Inputs
        
        ### `DBodyVector`
        
        - A _[DBodyVector](../data-type/psj-utility/pre-utility/built-in-types/BodyVector)_ object or _List of [DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_ objects storing the information of parts to be scaled.
        - This is a required input.
        
        ### `dlScaleVector`
        
        - A _List of Double_ specifying the scale vector. It defines how much scaling is used in each direction.
        - This is a required input.
        
        ### `dlScaleCenter`
        
        - A _List of Double_ specifying the scale center position. It defines a point where the scaling should be started.
        - This is a required input.
        
        ### `iColor`
        
        - An _Integer_ specifying the color of the previewed entity.
        - The default value is 255.
        
        ### `dTransparency`
        
        - A _Double_ specifying the transparency of the previewed entity.
        - The range of `dTransparency` = [0.0, 1.0]
        - The default value is 0.5.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {11}
        # Clear Preview
        JPT.ClearPreview()
        
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], strName="Cube_2", iPartColor=13259210)
        
        # Preview
        color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
        parts = JPT.GetAllParts()
        JPT.PreviewScaling(parts,[2.1,1.1,1.1],[0,0,0],color,0.2)
        JPT.ViewFitToModel()
        ```
        
        """
        message = "JPT.PreviewScaling({},{},{},{},{})".format(DBodyVector,dlScaleVector,dlScaleCenter,iColor,dTransparency)
        return JPT_RUN_LINE(message)

    def PreviewTranslation(DBodyVector, dlTranslationVector, iColor=255, dTransparency=0.5, DCoord=None):
        r"""
        ## Description
        
        Show preview result of body translation.
        
        ## Syntax
        
        ```psj
        JPT.PreviewTranslation(...)
        ```
        
        ## Inputs
        
        ### `DBodyVector`
        
        - A _[DBodyVector](../data-type/psj-utility/pre-utility/built-in-types/BodyVector)_ object or _List of [DBody](../data-type/psj-utility/pre-utility/built-in-types/DBody)_ objects storing the information of parts to be moved.
        - This is a required input.
        
        ### `dlTranslationVector`
        
        - A _List of Double_ specifying the translation vector defining the direction and magnitude of the translation.
        - This is a required input.
        
        ### `iColor`
        
        - An _Integer_ specifying the color of the previewed entity.
        - The default value is 255.
        
        ### `dTransparency`
        
        - A _Double_ specifying the transparency of the previewed entity.
        - The range of `dTransparency` = [0.0, 1.0]
        - The default value is 0.5.
        
        ### `DCoord`
        
        - A _[DCoord](../data-type/psj-utility/pre-utility/built-in-types/DCoord)_ object specifying Local Coordinate System.
        - The default value is None (Global Coordinate System).
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {13}
        # Clear Preview
        JPT.ClearPreview()
        
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], strName="Cube_2", iPartColor=13259210)
        Tools.Coordinates.ThreeNode(iOrder=-1, crlNodes=[Node(496, 578, 590)])
        
        # Preview
        color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
        parts = JPT.GetAllParts()
        coord = JPT.GetAllCoordinates()
        JPT.PreviewTranslation(parts,[0.02,0.01,0.01],color,1,coord[0])
        JPT.ViewFitToModel()
        ```
        
        """
        message = "JPT.PreviewTranslation({},{},{},{},{})".format(DBodyVector,dlTranslationVector,iColor,dTransparency,DCoord)
        return JPT_RUN_LINE(message)

    def PrintAppPathInfo():
        r"""
        ## Description
        
        Print all paths of the current Jupiter to the Jupiter API window, including:
        
        - Installation folder
        - Temp folder
        - Appdata folder
        - Current Jupiter file path
        
        ## Syntax
        
        ```psj
        JPT.PrintAppPathInfo()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {2}
        # Print all paths of the current Jupiter
        JPT.PrintAppPathInfo()
        ```
        
        """
        message = "JPT.PrintAppPathInfo({})".format('')
        return JPT_RUN_LINE(message)

    def PrintPSJUtilityManual():
        r"""
        ## Description
        
        Print all the information of all PSJ utilities to the Python API window.
        
        ## Syntax
        
        ```psj
        JPT.PrintPSJUtilityManual()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {2}
        # Print all the information of all PSJ utilities to the Python API Window
        JPT.PrintPSJUtilityManual()
        ```
        
        """
        message = "JPT.PrintPSJUtilityManual({})".format('')
        return JPT_RUN_LINE(message)

    def QuitApplication():
        r"""
        ## Description
        
        Quit Jupiter immediately.
        
        ## Syntax
        
        ```psj
        JPT.QuitApplication()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {2}
        # Quit Jupiter immediately
        JPT.QuitApplication()
        ```
        
        """
        message = "JPT.QuitApplication({})".format('')
        return JPT_RUN_LINE(message)

    def RemoveAllAbaqusStep():
        r"""
        ## Description
        
        Remove all the existing Abaqus steps.
        
        ## Syntax
        
        ```psj
        JPT.RemoveAllAbaqusStep()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {34}
        # Creating jobs with steps
        JPT.Exec('AbaqusStaticStep("Step1", "", 1, 100, 1, 1e-05, \
                  1, 0, 0, 0, 8, 1, 30, 0, 0.0002, 1, 0.05, 0, 1, 0, \
                  0, 1, 1, 0, 0, 0, 0, [""], [], 0:0)')
        JPT.Exec('AbaqusStaticStep("Step2", "", 1, 100, 1, 1e-05, \
                  1, 0, 0, 0, 8, 1, 30, 0, 0.0002, 1, 0.05, 0, 1, 0, \
                  0, 1, 1, 0, 0, 0, 0, [""], [], 0:0)')
        JPT.Exec('AbaqusStaticStep("Step3", "", 1, 100, 1, 1e-05, \
                  1, 0, 0, 0, 8, 1, 30, 0, 0.0002, 1, 0.05, 0, 1, 0, \
                  0, 1, 1, 0, 0, 0, 0, [""], [], 0:0)')
        JPT.Exec('AbaqusStaticStep("Step4", "", 1, 100, 1, 1e-05, \
                  1, 0, 0, 0, 8, 1, 30, 0, 0.0002, 1, 0.05, 0, 1, 0, \
                  0, 1, 1, 0, 0, 0, 0, [""], [], 0:0)')
        JPT.Exec('AbaqusStaticStep("Step5", "", 1, 100, 1, 1e-05, \
                  1, 0, 0, 0, 8, 1, 30, 0, 0.0002, 1, 0.05, 0, 1, 0, \
                  0, 1, 1, 0, 0, 0, 0, [""], [], 0:0)')
        JPT.Exec('AbaqusStaticStep("Step6", "", 1, 100, 1, 1e-05, \
                  1, 0, 0, 0, 8, 1, 30, 0, 0.0002, 1, 0.05, 0, 1, 0, \
                  0, 1, 1, 0, 0, 0, 0, [""], [], 0:0)')
        JPT.Exec('CreateAbaqusJob("Job_1", 0, 0, 0, 0, 1, 0, "", \
                  [134:1, 134:2, 134:3, 134:4, 134:5, 134:6], 0:0, \
                  [], 0, 0, 0, 0, 1, 0:0, 1)')
        JPT.Exec('AbaqusStaticStep("Step7", "", 1, 100, 1, 1e-05, \
                  1, 0, 0, 0, 8, 1, 30, 0, 0.0002, 1, 0.05, 0, 1, 0, \
                  0, 1, 1, 0, 0, 0, 0, [""], [], 0:0)')
        JPT.Exec('AbaqusStaticStep("Step8", "", 1, 100, 1, 1e-05, \
                  1, 0, 0, 0, 8, 1, 30, 0, 0.0002, 1, 0.05, 0, 1, 0, \
                  0, 1, 1, 0, 0, 0, 0, [""], [], 0:0)')
        JPT.Exec('CreateAbaqusJob("Job_2", 0, 0, 0, 0, 1, 0, "", \
                  [134:1, 134:2, 134:3, 134:4, 134:5, 134:6, 134:7, 134:8], 0:0, \
                  [], 0, 0, 0, 0, 1, 0:0, 1)')
        
        # Remove all the created steps for both created jobs
        JPT.RemoveAllAbaqusStep()
        ```
        
        """
        message = "JPT.RemoveAllAbaqusStep({})".format('')
        return JPT_RUN_LINE(message)

    def RemoveAllByTableType(DTableType):
        r"""
        ## Description
        
        Remove all the entities relating to the inputted _[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_.
        
        ## Syntax
        
        ```psj
        JPT.RemoveAllByTableType(DTableType)
        ```
        
        ## Inputs
        
        ### `DTableType`
        
        - An _Enum_ specifying the _[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_ of the entities which will be removed.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {9}
        # Prepare model
        Geometry.Part.Cube(iPartColor=5955674)
        Geometry.Part.Cube(strName="Cube_2", iPartColor=5682356)
        Geometry.Part.Cube(strName="Cube_3", iPartColor=12237393)
        Geometry.Part.Cube(strName="Cube_4", iPartColor=6740326)
        Geometry.Part.Cube(strName="Cube_5", iPartColor=7335919)
        
        # Remove all the created parts
        JPT.RemoveAllByTableType(JPT.DTableType.DTABLE_BODY)
        ```
        
        """
        message = "JPT.RemoveAllByTableType({})".format(DTableType)
        return JPT_RUN_LINE(message)

    def RemoveAllConnections():
        r"""
        ## Description
        
        Remove all the existing connections.
        
        ## Syntax
        
        ```psj
        JPT.RemoveAllConnections()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {50}
        # Prepare model
        Geometry.Part.Cube(iPartColor=7011837)
        Connections.RigidElements.RBE2.OneToMany(
            crlMasterTargets=[Node(446)], crlSlaveTargets=[Node(467)]
        )
        Connections.RigidElements.RBE2.OneToMany(
            crlMasterTargets=[Node(443)], crlSlaveTargets=[Node(470)], strName="RBE2_2"
        )
        Connections.RigidElements.RBE3.OneToMany(
            crlMasterTargets=[Node(450)],
            crlSlaveTargets=[Node(455)],
            listRbe3TermConnection=[(0, 63, 1), (1, 7, 1)],
            strName="RBE3_1",
        )
        Connections.RigidElements.RBE3.OneToMany(
            crlMasterTargets=[Node(463)],
            crlSlaveTargets=[Node(458)],
            listRbe3TermConnection=[(0, 63, 1), (1, 7, 1)],
            strName="RBE3_2",
        )
        Connections.MPC.General.NodesToNodes(
            crlMasterNodes=[Node(436)],
            crlSlaveNodes=[Node(476)],
            listMpcConnection=[
                MPC_CONNECTION(iDof=1),
                MPC_CONNECTION(iDof=2),
                MPC_CONNECTION(iDof=4),
                MPC_CONNECTION(),
                MPC_CONNECTION(),
                MPC_CONNECTION(),
            ],
            bUpdateDispCS=1,
        )
        Connections.MPC.General.NodesToNodes(
            strName="MPC_2",
            crlMasterNodes=[Node(437)],
            crlSlaveNodes=[Node(477)],
            listMpcConnection=[
                MPC_CONNECTION(iDof=1),
                MPC_CONNECTION(iDof=2),
                MPC_CONNECTION(iDof=4),
                MPC_CONNECTION(),
                MPC_CONNECTION(),
                MPC_CONNECTION(),
            ],
            bUpdateDispCS=1,
        )
        
        # Remove all created connections
        JPT.RemoveAllConnections()
        ```
        
        """
        message = "JPT.RemoveAllConnections({})".format('')
        return JPT_RUN_LINE(message)

    def RemoveAllContacts():
        r"""
        ## Description
        
        Remove all the existing contacts.
        
        ## Syntax
        
        ```psj
        JPT.RemoveAllContacts()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {65}
        # Prepare model
        Geometry.Part.Cube(iPartColor=7011837)
        Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0], strName="Cube_2", iPartColor=6351851)
        Geometry.Part.Cube(dlOrigin=[0.04, 0.0, 0.0], strName="Cube_3", iPartColor=16543085)
        Geometry.Part.Cube(dlOrigin=[0.04, 0.01, 0.0], strName="Cube_4", iPartColor=11948369)
        Geometry.Part.Cube(dlOrigin=[0.02, 0.01, 0.0], strName="Cube_5", iPartColor=12079955)
        Geometry.Part.Cube(dlOrigin=[0.02, 0.01, 0.01], strName="Cube_6", iPartColor=14837474)
        Tools.Group.CreateGroup(strGroupName="Cube_5-G0001", crlTargets=[Face(130)])
        Tools.Group.CreateGroup(strGroupName="Cube_6-G0002", crlTargets=[Face(155)])
        Connections.Contacts.Abaqus.ContactTable(
            strName="C0001_Cube_5-G0001_Cube_6-G0002",
            iContactType=1,
            dAdjustWidth=DFLT_DBL,
            dExtensionZone=DFLT_DBL,
            dMaxPenetration=DFLT_DBL,
            dSmoothAngle=DFLT_DBL,
            iFrictionType=-1,
            dFrictionCoeff1=DFLT_DBL,
            dFrictionCoeff2=DFLT_DBL,
            dShearStressLimit=DFLT_DBL,
            dSlipTolerance=DFLT_DBL,
            dStaticFrictionCoeff=DFLT_DBL,
            dKineticFrictionCoeff=DFLT_DBL,
            dDecayCoeff=DFLT_DBL,
            bAdjustPosition=True,
            dPositionTolerance=DFLT_DBL,
            iFormulationType=-1,
            iPressureOverclosureType=-1,
            dContactStiffness=DFLT_DBL,
            tshPressureOverclosure=[0, 0],
            tshClearanceData=[1, 2, DFLT_DBL, DFLT_DBL],
            tshPressureData=[1, 2, DFLT_DBL, DFLT_DBL],
            crplTargets=[CursorPair(Group(1), Group(2))],
            iContactColor=65280,
        )
        Tools.Group.CreateGroup(strGroupName="Cube_5-G0004", crlTargets=[Face(125)])
        Tools.Group.CreateGroup(strGroupName="Cube_2-G0003", crlTargets=[Face(48)])
        Connections.Contacts.Abaqus.ContactTable(
            strName="C0002_Cube_5-G0004_Cube_2-G0003",
            iContactType=1,
            dAdjustWidth=DFLT_DBL,
            dExtensionZone=DFLT_DBL,
            dMaxPenetration=DFLT_DBL,
            dSmoothAngle=DFLT_DBL,
            iFrictionType=-1,
            dFrictionCoeff1=DFLT_DBL,
            dFrictionCoeff2=DFLT_DBL,
            dShearStressLimit=DFLT_DBL,
            dSlipTolerance=DFLT_DBL,
            dStaticFrictionCoeff=DFLT_DBL,
            dKineticFrictionCoeff=DFLT_DBL,
            dDecayCoeff=DFLT_DBL,
            bAdjustPosition=True,
            dPositionTolerance=DFLT_DBL,
            iFormulationType=-1,
            iPressureOverclosureType=-1,
            dContactStiffness=DFLT_DBL,
            tshPressureOverclosure=[0, 0],
            tshClearanceData=[1, 2, DFLT_DBL, DFLT_DBL],
            tshPressureData=[1, 2, DFLT_DBL, DFLT_DBL],
            crplTargets=[CursorPair(Group(3), Group(4))],
            iContactColor=65280,
        )
        # Remove all created contacts (Here is Abaqus's contact type)
        JPT.RemoveAllContacts()
        ```
        
        """
        message = "JPT.RemoveAllContacts({})".format('')
        return JPT_RUN_LINE(message)

    def RemoveAllCoordinates():
        r"""
        ## Description
        
        Remove all the existing local coordinate systems.
        
        ## Syntax
        
        ```psj
        JPT.RemoveAllCoordinates()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {9}
        # Prepare model
        Geometry.Part.Cube()
        Tools.Coordinates.ThreeNode(crlNodes=[Node(436, 452, 438)])
        Tools.Coordinates.ThreeNode(strName="CRect2", crlNodes=[Node(7, 93, 86)])
        Tools.Coordinates.ThreeNode(strName="CCyl1", iCoordType=1, crlNodes=[Node(22, 3, 31)])
        Tools.Coordinates.ThreeNode(strName="CSph1", iCoordType=2, crlNodes=[Node(4, 26, 39)])
        
        # Delete all the created coordinates
        JPT.RemoveAllCoordinates()
        ```
        
        """
        message = "JPT.RemoveAllCoordinates({})".format('')
        return JPT_RUN_LINE(message)

    def RemoveAllFieldTables():
        r"""
        ## Description
        
        Remove all the existing field tables.
        
        ## Syntax
        
        ```psj
        JPT.RemoveAllFieldTables()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {10}
        # Create sample fields data
        BoundaryConditions.FieldData(strName="test_1", iType=1,
                                     ilSheet=[3, 4, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3])
        BoundaryConditions.FieldData(strName="test_2", iType=4,
                                     ilSheet=[3, 2, 1, 1, 2, 2, 3, 3])
        BoundaryConditions.FieldData(strName="test_3", iType=3,
                                     ilSheet=[3, 2, 1, 1, 2, 2, 3, 3])
        
        # Remove all the created fields data
        JPT.RemoveAllFieldTables()
        ```
        
        """
        message = "JPT.RemoveAllFieldTables({})".format('')
        return JPT_RUN_LINE(message)

    def RemoveAllLoadCases():
        r"""
        ## Description
        
        Remove all the existing load cases.
        
        ## Syntax
        
        ```psj
        JPT.RemoveAllLoadCases()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {31}
        # Prepare model
        Geometry.Part.Cube(iPartColor=13259210)
        Geometry.Part.Cube(dlOrigin=[0.04, 0.0, 0.0], strName="Cube_2", iPartColor=7697908)
        Geometry.Part.Cube(dlOrigin=[0.08, 0.0, 0.0], strName="Cube_3", iPartColor=7463537)
        BoundaryConditions.FixedConstraint(crlTargets=[Face(78, 52)])
        BoundaryConditions.FixedConstraint(strName="Constraint2", crlTargets=[Face(50)])
        BoundaryConditions.FixedConstraint(strName="Constraint3", crlTargets=[Face(24)])
        BoundaryConditions.FixedConstraint(strName="Constraint4", crlTargets=[Face(26)])
        BoundaryConditions.Pressure.General(crlTargets=[Face(51)])
        BoundaryConditions.Pressure.General(strName="Pressure2", crlTargets=[Face(77)])
        BoundaryConditions.Pressure.General(strName="Pressure3", crlTargets=[Face(25)])
        BoundaryConditions.Force.General("Force1",
                                         forceLBC=FORCE_LBC(vecForce=[1.0, DFLT_DBL, DFLT_DBL]),
                                         crlTargets=[Face(22)])
        BoundaryConditions.Force.General("Force2",
                                         forceLBC=FORCE_LBC(vecForce=[1.0, DFLT_DBL, DFLT_DBL]),
                                         crlTargets=[Face(48)])
        BoundaryConditions.Force.General("Force3",
                                         forceLBC=FORCE_LBC(vecForce=[1.0, DFLT_DBL, DFLT_DBL]),
                                         crlTargets=[Face(74)])
        BoundaryConditions.LoadCase(crlTargets=[LbcConstraint(1, 2)],
                                    iExportId=5, dlTargetFactor=[1.0, 1.0])
        BoundaryConditions.LoadCase(strName="LoadCase2",
                                    crlTargets=[LbcConstraint(1, 3)], iExportId=6,
                                    dlTargetFactor=[1.0, 1.0])
        BoundaryConditions.LoadCase(strName="LoadCase3",
                                    crlTargets=[LbcConstraint(2, 3)], iExportId=7,
                                    dlTargetFactor=[1.0, 1.0])
        
        # Remove all the created load cases
        JPT.RemoveAllLoadCases()
        ```
        
        """
        message = "JPT.RemoveAllLoadCases({})".format('')
        return JPT_RUN_LINE(message)

    def RemoveAllLoadsBCs():
        r"""
        ## Description
        
        Remove all the existing loads and boundary conditions.
        
        ## Syntax
        
        ```psj
        JPT.RemoveAllLoadsBCs()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {23}
        # Prepare model
        Geometry.Part.Cube(iPartColor=13259210)
        Geometry.Part.Cube(dlOrigin=[0.04, 0.0, 0.0], strName="Cube_2", iPartColor=7697908)
        Geometry.Part.Cube(dlOrigin=[0.08, 0.0, 0.0], strName="Cube_3", iPartColor=7463537)
        BoundaryConditions.FixedConstraint(crlTargets=[Face(78, 52)])
        BoundaryConditions.FixedConstraint(strName="Constraint2", crlTargets=[Face(50)])
        BoundaryConditions.FixedConstraint(strName="Constraint3", crlTargets=[Face(24)])
        BoundaryConditions.FixedConstraint(strName="Constraint4", crlTargets=[Face(26)])
        BoundaryConditions.Pressure.General(crlTargets=[Face(51)])
        BoundaryConditions.Pressure.General(strName="Pressure2", crlTargets=[Face(77)])
        BoundaryConditions.Pressure.General(strName="Pressure3", crlTargets=[Face(25)])
        BoundaryConditions.Force.General("Force1",
                                         forceLBC=FORCE_LBC(vecForce=[1.0, DFLT_DBL, DFLT_DBL]),
                                         crlTargets=[Face(22)])
        BoundaryConditions.Force.General("Force2",
                                         forceLBC=FORCE_LBC(vecForce=[1.0, DFLT_DBL, DFLT_DBL]),
                                         crlTargets=[Face(48)])
        BoundaryConditions.Force.General("Force3",
                                         forceLBC=FORCE_LBC(vecForce=[1.0, DFLT_DBL, DFLT_DBL]),
                                         crlTargets=[Face(74)])
        
        # Remove all the created loads and boundary conditions
        JPT.RemoveAllLoadsBCs()
        ```
        
        """
        message = "JPT.RemoveAllLoadsBCs({})".format('')
        return JPT_RUN_LINE(message)

    def RemoveAllMaterials():
        r"""
        ## Description
        
        Remove all the existing material in the User material database.
        
        ## Syntax
        
        ```psj
        JPT.RemoveAllMaterials()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {13}
        # Create materials
        Properties.Material.Add("Copper_Alloy", [Density([(DENSITY, 8.3e-09)]),
                                                 Elastic([(YOUNGS_MODULUS, 110000.0),
                                                          (POISSONS_RATIO, 0.34)])])
        Properties.Material.Add("Stainless_Steel", [Density([(DENSITY, 7.75e-09)]),
                                                    Elastic([(YOUNGS_MODULUS, 193000.0),
                                                             (POISSONS_RATIO, 0.31)])])
        Properties.Material.Add("Titanium_Alloy", [Density([(DENSITY, 4.62e-09)]),
                                                   Elastic([(YOUNGS_MODULUS, 96000.0),
                                                            (POISSONS_RATIO, 0.36)])])
        
        # Remove all the created materials in the User material database
        JPT.RemoveAllMaterials()
        ```
        
        """
        message = "JPT.RemoveAllMaterials({})".format('')
        return JPT_RUN_LINE(message)

    def RemoveAllMeshSettings():
        r"""
        ## Description
        
        Remove all the existing local mesh settings.
        
        ## Syntax
        
        ```psj
        JPT.RemoveAllMeshSettings()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {30}
        # Prepare model
        Geometry.Part.Cube(iPartColor=5688524)
        Meshing.LocalSettings.Face(strName="MeshParam_1",
                                   localMesh=LOCAL_MESH(iEntityType=2,
                                                        bEnableSizeParams=True,
                                                        dAvgElemSize=0.005,
                                                        dMaxElemSize=0.01,
                                                        dMinElemSize=0.001,
                                                        bEnableMeshPattern=True,
                                                        iMeshPatternType=1),
                                   crlTargets=[Face(26)])
        Meshing.LocalSettings.Edge(strName="MeshParam_2",
                                   localMesh=LOCAL_MESH(iEntityType=3,
                                                        dAvgElemSize=0.005,
                                                        dMaxElemSize=0.01,
                                                        dMinElemSize=0.001,
                                                        dTrimAngle=0.7853981634,
                                                        bEnableMeshCount=True,
                                                        iNodeCount=1),
                                   crlTargets=[Edge(18, 17, 19)])
        Meshing.LocalSettings.Part(strName="MeshParam_3",
                                   localMesh=LOCAL_MESH(iEntityType=1,
                                                        bEnableSizeParams=True,
                                                        dAvgElemSize=0.005,
                                                        dMaxElemSize=0.01,
                                                        dMinElemSize=0.001),
                                   crlTargets=[Part(1)])
        
        # Delete all the created local meshing
        JPT.RemoveAllMeshSettings()
        ```
        
        """
        message = "JPT.RemoveAllMeshSettings({})".format('')
        return JPT_RUN_LINE(message)

    def RemoveAllSolverjob():
        r"""
        ## Description
        
        Remove all the existing solver jobs (Analysis jobs).
        
        ## Syntax
        
        ```psj
        JPT.RemoveAllSolverjob()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {33}
        # Create solver jobs
        JPT.Exec('Nastran_LinearStatic("Job_1", "", [], 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, \
                                       1.79769e+308, 2147483647, 0, 2147483647, 0, 1, 101, "", \
                                       [1.79769e+308, 1.79769e+308, 2147483647], [0, 1.79769e+308, \
                                       1.79769e+308, 2147483647, 0, 0, 1.79769e+308, 1.79769e+308, \
                                       2147483647], [1.79769e+308, 1.79769e+308, 2147483647, 0], \
                                       [2147483647, 1.79769e+308, 2147483647, 2, 0], [2147483647, \
                                       2147483647, 2147483647, 2147483647, 2147483647, 2147483647, \
                                       2147483647, 0, 0, 2147483647, 0, 2147483647, 2147483647, 0, \
                                       0, 0, 0, 2147483647, 2147483647, 1, 0, 0, 0, 1, 0, 0, 0, 0, \
                                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0], [0, ""], [2147483647, \
                                       2147483647, 2147483647, 2147483647, 2147483647, 2147483647], \
                                       [-1, 0, 0, "", "", "", "", 2147483647, 2, 0, 1.79769e+308, \
                                       1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 0, \
                                       2147483647, 1, 0], [1, 3, 1, 0, 0, 1, 0.01, 0.01, 0.01], \
                                       [2147483647, 1.79769e+308, 2147483647], [], "", "", "", "", \
                                       "", 0, 1, 0, 0:0, "", 0, 0)')
        JPT.Exec('CreateAbaqusJob("Job_3", 0, 0, 0, 0, 1, 0, "", [], 0:0, [], 0, 0, 0, 0, 1, 0:0, 1)')
        JPT.Exec('TSSolverLinearStatic("Job_4", "", [], 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1.79769e+308, 2147483647, \
                                       0, 1024, 0, 0, 101, "", [1.79769e+308, 1.79769e+308, 2147483647], [0, \
                                       1.79769e+308, 1.79769e+308, 2147483647, 0, 0, 1.79769e+308, 1.79769e+308, \
                                       2147483647], [1.79769e+308, 1.79769e+308, 2147483647, 0], [2147483647, \
                                       1.79769e+308, 2147483647, 2, 0], [2147483647, 2147483647, 2147483647, \
                                       2147483647, 2147483647, 2147483647, 2147483647, 0, 0, 2147483647, 0, 0, 0, \
                                       0, 0, 0, 0, 2147483647, 2147483647, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, \
                                       0, 0, 0, 0, 0, 0], [0], [0, ""], [2147483647, 2147483647, 2147483647, 2147483647, \
                                       2147483647, 2147483647], [-1, 0, 0, "", "", "", "", 2147483647, 2, 0, 1.79769e+308, \
                                       1.79769e+308, 1.79769e+308, 1.79769e+308, 1.79769e+308, 0, 2147483647, 1, 0], [1, \
                                       3, 2147483647, 0, 0, 1, 1.79769e+308, 1.79769e+308, 0.01], [2147483647, 1.79769e+308, \
                                       2147483647], [], "", "", "", "", "", 0, 0:0, "")')
        
        # Remove all the created solver jobs
        JPT.RemoveAllSolverjob()
        ```
        
        """
        message = "JPT.RemoveAllSolverjob({})".format('')
        return JPT_RUN_LINE(message)

    def RemoveEntitiesByID(DItemType, itemID):
        r"""
        ## Description
        
        Remove specified entity by inputting its DItem type and its ID.
        
        ## Syntax
        
        ```psj
        JPT.RemoveEntitiesByID(DItemType, itemID)
        ```
        
        ## Inputs
        
        ### `DItemType`
        
        - An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.
        - This is a required input.
        
        ### `itemID`
        
        - An _Integer_ specifying the ID of the target entity to be removed.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {8}
        # Prepare model
        Geometry.Part.Cube(iPartColor=12829526)
        Geometry.Part.Cube(strName="Cube_2", iPartColor=8060538)
        Geometry.Part.Cube(strName="Cube_3", iPartColor=13787489)
        JPT.ViewFitToModel()
        
        # Delete Cube_2 part
        JPT.RemoveEntitiesByID(JPT.DItemType.BODY, 2)
        ```
        
        """
        message = "JPT.RemoveEntitiesByID({},{})".format(DItemType,itemID)
        return JPT_RUN_LINE(message)

    def RemoveEntitiesByName(DTableType, itemName, BoolType):
        r"""
        ## Description
        
        Remove entities by using the inputted name.
        
        ## Syntax
        
        ```psj
        JPT.RemoveEntitiesByName(DTableType, itemName, BoolType)
        ```
        
        ## Inputs
        
        ### `DTableType`
        
        - An _Enum_ specifying the _[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_ of entity in Jupiter.
        - This is a required input.
        
        ### `itemName`
        
        - A _String_ specifying the name of the target entity to be removed.
        - This is a required input.
        
        ### `BoolType`
        
        - An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the matching type:
          - _False_: Approximate match.
          - _True_: Exact match.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {8}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Remove all the parts with their name have the "_" character inside
        JPT.RemoveEntitiesByName(JPT.DTableType.DTABLE_BODY, "_", JPT.BoolType.FALSE_VAL)
        ```
        
        """
        message = "JPT.RemoveEntitiesByName({},{},{})".format(DTableType,itemName,BoolType)
        return JPT_RUN_LINE(message)

    def RemoveWSProperties():
        r"""
        ## Description
        
        Remove all the existing applied properties.
        
        ## Syntax
        
        ```psj
        JPT.RemoveWSProperties()
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {26}
        # Prepare model
        Geometry.Part.Cube(iPartColor=6475470)
        Geometry.Part.Cube(strName="Cube_2", iPartColor=7794157)
        Geometry.Part.Cube(strName="Cube_3", iPartColor=6081483)
        Geometry.Part.Cube(strName="Cube_4", iPartColor=6613224)
        Meshing.SolidMeshing(crlParts=[Part(1, 2, 3, 4)], bTet10=True, dGradingFactor=1.05,
                             dStretchLimit=0.1, iSpeedVsQual=1, iRegion=1, bSafeMode=False,
                             iParallel=12, bInternalMeshOnly=False, iPartColor=65280)
        Properties.Material.Add("Copper_Alloy", [Density([(DENSITY, 8.3e-09)]),
                                Elastic([(YOUNGS_MODULUS, 110000.0),
                                         (POISSONS_RATIO, 0.34)])])
        Properties.Solid(strName="Solid Property 1", crMaterial=Material(1), iCordM=-2,
                         dDynaRemeshVal1=DFLT_DBL, dDynaRemeshVal2=DFLT_DBL, dDispHG=DFLT_DBL,
                         crlTargets=[Part(1)], iFLG=-1)
        Properties.Solid(strName="Solid Property 2", iPropertyId=2, crMaterial=Material(1), iCordM=-2,
                         dDynaRemeshVal1=DFLT_DBL, dDynaRemeshVal2=DFLT_DBL, dDispHG=DFLT_DBL,
                         crlTargets=[Part(2)], iFLG=-1)
        Properties.Solid(strName="Solid Property 3", iPropertyId=3, crMaterial=Material(1), iCordM=-2,
                         dDynaRemeshVal1=DFLT_DBL, dDynaRemeshVal2=DFLT_DBL, dDispHG=DFLT_DBL,
                         crlTargets=[Part(3)], iFLG=-1)
        Properties.Solid(strName="Solid Property 4", iPropertyId=4, crMaterial=Material(1), iCordM=-2,
                         dDynaRemeshVal1=DFLT_DBL, dDynaRemeshVal2=DFLT_DBL, dDispHG=DFLT_DBL,
                         crlTargets=[Part(4)], iFLG=-1)
        
        # Remove all the created properties
        JPT.RemoveWSProperties()
        ```
        
        """
        message = "JPT.RemoveWSProperties({})".format('')
        return JPT_RUN_LINE(message)

    def RunSunShine(InputFile, OutputFolder="", Memory=2.0, Threads=1, KeepTemp=False, WriteDatabase=False, ShowProgress=False):
        r"""
        ## Description
        
        Run SunShine to solve an analysis problem.
        
        ## Syntax
        
        ```psj
        JPT.RunSunShine(...)
        ```
        
        ## Inputs
        
        ### `InputFile`
        
        - A _String_ specifying the path of solver input file will be solved.
        - This is a required input.
        
        ### `OutputFolder`
        
        - A _String_ specifying the path of folder to store the result files.
        - The default value is "" (the folder where the input file is located).
        
        ### `Memory`
        
        - A _Double_ specifying the size of memory in GB to be used in execution.
        - The default value is 2.0 (GB).
        
        ### `Threads`
        
        - A _Integer_ specifying the number of threads to be used in execution.
        - The default value is 1.
        
        ### `KeepTemp`
        
        - A _Boolean_ specifying whether to keep the temporary files after termination of execution.
        - The default value is False.
        
        ### `WriteDatabase`
        
        - A _Boolean_ specifying whether to keep the temporary files after termination of execution.
        - The default value is False.
        
        ### `ShowProgress`
        
        - A _Boolean_ specifying whether to keep the temporary files after termination of execution.
        - The default value is False.
        
        ## Return Code
        
        - Boolean specifying whether the process is executed successfully or not:
          - True: The process is executed successfully.
          - False: Cannot execute the function.
        
        ## Sample Code
        
        ```psj {63-69}
        # Prepare model
        Geometry.Part.Cube(dlLength=[0.01, 0.01, 0.1], iPartColor=7463537)
        Meshing.SetMeshAttribute(crlParts=[Part(1)], 
                                surfaceMesh=SURFACE_MESH(dMaxElemSize=0.4, 
                                  dGeomAngle=0.7853981634, 
                                  iPerformanceMode=1, 
                                  dAutoMergeTinyFacesAngle=0.5235987756, 
                                  bGeomApprox=True, 
                                  iNextEntityOffsetId=0))
        Meshing.SurfaceMeshing(crlParts=[Part(1)], 
                              surfaceMesh=SURFACE_MESH(dMaxElemSize=0.4, 
                                dGeomAngle=0.7853981634, 
                                iPerformanceMode=1, 
                                dAutoMergeTinyFacesAngle=0.5235987756, 
                                bGeomApprox=True, 
                                iNextEntityOffsetId=0), 
                              iThreadNum=16)
        Meshing.SolidMeshing(crlParts=[Part(1)], 
                            dGradingFactor=1.05, 
                            dStretchLimit=0.1, 
                            iSpeedVsQual=1, 
                            iRegion=1, 
                            bSafeMode=False, 
                            iParallel=16, 
                            bInternalMeshOnly=False, 
                            iPartColor=65280)
        BoundaryConditions.FixedConstraint(strName="Constraint_1", crlTargets=[Face(25)])
        BoundaryConditions.Force.General(strName="Force_1", 
                                        forceLBC=FORCE_LBC(vecForce=[DFLT_DBL, DFLT_DBL, 100.0]), 
                                          crlTargets=[Face(26)])
        Properties.Material.Add(strMaterialName="Structural_Steel",
                               dictMaterialProperty={
                                'Density': {'density': {'DENSITY': [7850.000000000001]}}, 
                                'Elastic': {'elastic': {'YOUNGS_MODULUS': [200000000000.0], 
                                'POISSONS_RATIO': [0.3]}}, 
                                'Expansion': {'expansion': {'ALPHA': [1.2e-05]}}, 
                                'Conductivity': {'conductivity': {'CONDUCTIVITY': [59.0]}}, 
                                'SpecificHeat': {'specificHeat': {'SPECIFIC_HEAT': [461.0]}}}, 
                              iMaterialID=5, 
                              iMaterialColor=10264731)
        Properties.Solid(crlTargets=[Part(1)], 
                        strName="SolidProperty_1",
                        iPropertyColor=959547, 
                        crMaterial=Material(5), 
                        iCordM=-2, 
                        dDynaRemeshVal1=DFLT_DBL, 
                        dDynaRemeshVal2=DFLT_DBL, 
                        dDispHG=DFLT_DBL, 
                        iFLG=-1)
        Analysis.TSSS.LinearStatic(
                                  nastranAnalysis=NASTRAN_ANALYSIS(
                                    iSolverType=6, 
                                    iGridFormatType=1, 
                                    dEpsilon=DFLT_DBL, 
                                    iMaxNumOfIter=DFLT_INT, 
                                    iNumberOfThreads=1, 
                                    iMemory=2, 
                                    iNcpu=DFLT_INT, 
                                    iSolNo=101, 
                                    nastranOutputRequest=NASTRAN_OUTPUT_REQUEST(iTypeStrain=0)), 
                                  strPath="C:/temp/SOL_101.bdf")
        # Run SunShine to solve the problem
        progress = JPT.RunSunShine(r"C:\\temp\\SOL_101.bdf",
                                  "",
                                  2,
                                  1,
                                  False,
                                  True,
                                  False)
        if progress == True:
          print("SunShine succeeded, can start a new document and import the result...")
        else:
          print("SunShine failed")
        ```
        
        """
        message = "JPT.RunSunShine({},{},{},{},{},{},{})".format(InputFile,OutputFolder,Memory,Threads,KeepTemp,WriteDatabase,ShowProgress)
        return JPT_RUN_LINE(message)

    def SaveToMLIB(strFileName, bAppendToCurrentMlib, crlMaterials=[]):
        r"""
        ## Description
        
        Save materials in document to .mlib file.
        
        ## Syntax
        
        ```psj
        JPT.SaveToMLIB(...)
        ```
        
        ## Inputs
        
        ### `strFileName`
        
        - A _String_ sspecifying the path of .mlib file to save.
        - This is a required input.
          
        ### `bAppendToCurrentMlib`
        
        - A _Boolean_ specifying whether the materials in current library also copied in the .mlib file.
        - This is a required input.
        
        ### `crlMaterials`
        
        - A _List of Cursor_ specifying the materials needed to save.
        - The default value is [].
          
        ## Return Code
        
        - _True_ : The function can be executed
        - _False_ : The function cannot be executed
        
        ## Sample Code
        
        ```psj {34}
        # Create materials in User Data Base.
        Properties.Material.Add(
            strMaterialName="MyMaterial1",
            dictMaterialProperty={
                'Density': {
                    'density': {
                        'DENSITY': [8300.0]}}, 
                'Elastic': {
                    'elastic': {
                        'YOUNGS_MODULUS': [110000000000.0], 
                        'POISSONS_RATIO': [0.34]}}}, 
            iMaterialID=1, 
            iMaterialColor=7901428)
        
        Properties.Material.Add(
            strMaterialName="MyMaterial2", 
            dictMaterialProperty={
                'Density': {
                    'density': {
                        'DENSITY': [2770.0]}}, 
                'Elastic': {
                    'elastic': {
                        'YOUNGS_MODULUS': [71000000000.0], 
                        'POISSONS_RATIO': [0.33]}}}, 
             iMaterialID=2, 
            iMaterialColor=11052963)
        
        # Get all materials from current user data base. 
        strCrlMaterials=[mat.id for mat in JPT.GetAllMaterials()]
        strMlibFileName = "C:/Temp/new.mlib" 
        
        crlMaterials=Material(*[mat.id for mat in JPT.GetAllMaterials()])
        
        JPT.SaveToMLIB(
            strFileName=strMlibFileName, 
            crlMaterials=[crlMaterials], 
            bAppendToCurrentMlib=True # Include all the materials in Library Data Base
        )
        ```
        
        """
        message = "JPT.SaveToMLIB('{}',{},{})".format(strFileName,bAppendToCurrentMlib,crlMaterials)
        return JPT_RUN_LINE(message)

    def SelectionByID(DItemType, entityID, BoolType):
        r"""
        ## Description
        
        Select an entity by using its ID.
        
        ## Syntax
        
        ```psj
        JPT.SelectionByID(DItemType, entityID, BoolType)
        ```
        
        ## Inputs
        
        ### `DItemType`
        
        - An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.
        - This is a required input.
        
        ### `entityID`
        
        - An _Integer_ specifying ID of the selecting entity.
        - This is a required input.
        
        ### `BoolType`
        
        - An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the selection mode:
          - _True_: Select the inputted entity with its ID.
          - _False_: Deselect the inputted entity with its ID.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {7}
        # Prepare model
        Geometry.Part.Cube(iPartColor=6974164)
        Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=7599987)
        JPT.ViewFitToModel()
        
        # Select face with ID = 51
        JPT.SelectionByID(JPT.DItemType.FACE, 51, JPT.BoolType.TRUE_VAL)
        ```
        
        """
        message = "JPT.SelectionByID({},{},{})".format(DItemType,entityID,BoolType)
        return JPT_RUN_LINE(message)

    def SelectionByIDs(DItemType, entityIDs, BoolType):
        r"""
        ## Description
        
        Select entities by using their list of IDs.
        
        ## Syntax
        
        ```psj
        JPT.SelectionByIDs(DItemType, entityIDs, BoolType)
        ```
        
        ## Inputs
        
        ### `DItemType`
        
        - An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.
        - This is a required input.
        
        ### `entityIDs`
        
        - An _List of Integer_ specifying the list of ID of the selecting entites.
        - This is a required input.
        
        ### `BoolType`
        
        - An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the selection mode:
          - _True_: Select the inputted entity with its ID.
          - _False_: Deselect the inputted entity with its ID.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {7}
        # Prepare model
        Geometry.Part.Cube(iPartColor=6974164)
        Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=7599987)
        JPT.ViewFitToModel()
        
        # Select face with IDs = [50, 51, 52]
        JPT.SelectionByIDs(JPT.DItemType.FACE, [50, 51, 52], JPT.BoolType.TRUE_VAL)
        ```
        
        """
        message = "JPT.SelectionByIDs({},{},{})".format(DItemType,entityIDs,BoolType)
        return JPT_RUN_LINE(message)

    def SelectionByType(DItemType, BoolType):
        r"""
        ## Description
        
        Select all the existing entities by type.
        
        ## Syntax
        
        ```psj
        JPT.SelectionByType(DItemType, BoolType)
        ```
        
        ## Inputs
        
        ### `DItemType`
        
        - An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ of entity in Jupiter.
        - This is a required input.
        
        ### `BoolType`
        
        - An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the selection mode:
          - _True_: Select the inputted entity with its ID.
          - _False_: Deselect the inputted entity with its ID.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {6}
        # Prepare model
        Geometry.Part.Cube(iPartColor=6974164)
        Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=7599987)
        
        # Select all the created parts
        JPT.SelectionByType(JPT.DItemType.BODY, JPT.BoolType.TRUE_VAL)
        ```
        
        """
        message = "JPT.SelectionByType({},{})".format(DItemType,BoolType)
        return JPT_RUN_LINE(message)

    def SetActiveDocumentByID(docID, BoolType):
        r"""
        ## Description
        
        Set indicated document in active by using its ID.
        
        ## Syntax
        
        ```psj
        JPT.SetActiveDocumentByID(docID, BoolType)
        ```
        
        ## Inputs
        
        ### `docID`
        
        - A _String_ specifying the ID of document to activate.
        - This is a required input.
        
        ### `BoolType`
        
        - An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the selection mode:
          - _True_: Activate the indicated document.
          - _False_: Do not activate the indicated document.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {3}
        doc1 = JPT.CreateNewDocument()
        doc2 = JPT.CreateNewDocument()
        JPT.SetActiveDocumentByID(doc1.docID, 1)
        Geometry.Part.Cube()
        JPT.ViewFitToModel()
        ```
        
        """
        message = "JPT.SetActiveDocumentByID({},{})".format(docID,BoolType)
        return JPT_RUN_LINE(message)

    def SetActiveDocumentByName(docName, BoolType):
        r"""
        ## Description
        
        Set indicated document in active by using its name.
        
        ## Syntax
        
        ```psj
        JPT.SetActiveDocumentByName(docName, BoolType)
        ```
        
        ## Inputs
        
        ### `docName`
        
        - A _String_ specifying the name of document to activate.
        - This is a required input.
        
        ### `BoolType`
        
        - An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the selection mode:
          - _True_: Activate the indicated document.
          - _False_: Do not activate the indicated document.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {4}
        doc1 = JPT.CreateNewDocument()
        doc2 = JPT.CreateNewDocument()
        doc3 = JPT.CreateNewDocument()
        JPT.SetActiveDocumentByName(doc2.docName,1)
        Geometry.Part.Cube()
        JPT.ViewFitToModel()
        print("Created a Cube in " + str(doc2.docName) + " document")
        ```
        
        """
        message = "JPT.SetActiveDocumentByName({},{})".format(docName,BoolType)
        return JPT_RUN_LINE(message)

    def SetSelectMethod(selectMethodType):
        r"""
        ## Description
        
        Change the selection method in Jupiter to the specified one.
        
        ## Syntax
        
        ```psj
        JPT.SetSelectMethod(selectMethodType)
        ```
        
        ## Inputs
        
        ### `selectMethodType`
        
        - An _Enum_ specifying the _[SelectMethodType](../data-type/psj-utility/pre-utility/enumeration-types/select-method-types)_ describing the selection method.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {2,5,8,11}
        # Select method to Body selection
        JPT.SetSelectMethod(JPT.SelectMethodType.SELMTD_BODY)
        
        # Select method to Face selection
        JPT.SetSelectMethod(JPT.SelectMethodType.SELMTD_FACE)
        
        # Select method to Edge selection
        JPT.SetSelectMethod(JPT.SelectMethodType.SELMTD_EDGE)
        
        # Select method to Node selection
        JPT.SetSelectMethod(JPT.SelectMethodType.SELMTD_NODE)
        ```
        
        """
        message = "JPT.SetSelectMethod({})".format(selectMethodType)
        return JPT_RUN_LINE(message)

    def ShowHideAllParts(BoolType):
        r"""
        ## Description
        
        Show or Hide all part existing on the screen.
        
        ## Syntax
        
        ```psj
        JPT.ShowHideAllParts(BoolType)
        ```
        
        ## Inputs
        
        ### `BoolType`
        
        - An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the display mode:
          - _False_: Hide all parts.
          - _True_: Show all parts.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {8}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Show all parts
        JPT.ShowHideAllParts(JPT.BoolType.TRUE_VAL)
        ```
        
        """
        message = "JPT.ShowHideAllParts({})".format(BoolType)
        return JPT_RUN_LINE(message)

    def ShowHideEntitiesByID(DTableType, itemID, BoolType):
        r"""
        ## Description
        
        Show or Hide an entity by inputted its ID.
        
        ## Syntax
        
        ```psj
        JPT.ShowHideEntitiesByID(DTableType, itemID, BoolType)
        ```
        
        ## Inputs
        
        ### `DTableType`
        
        - An _Enum_ specifying the _[DTableType](../data-type/psj-utility/pre-utility/enumeration-types/dtable-types)_ of the entities which will be shown/hidden.
        - This is a required input.
        
        ### `itemID`
        
        - An _Integer_ specifying the ID of the target entity.
        - This is a required input.
        
        ### `BoolType`
        
        - An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the display mode:
          - _False_: Hide the inputted part.
          - _True_: Show the inputted part.
        - This is a required input.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {11}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(strName="Cube_2")
        Geometry.Part.Cube(strName="Cube_3")
        JPT.ViewFitToModel()
        
        # Hide all parts
        JPT.ShowHideAllParts(JPT.BoolType.FALSE_VAL)
        
        # Show Cube_1
        JPT.ShowHideEntitiesByID(JPT.DTableType.DTABLE_BODY, 1, JPT.BoolType.TRUE_VAL)
        ```
        
        """
        message = "JPT.ShowHideEntitiesByID({},{},{})".format(DTableType,itemID,BoolType)
        return JPT_RUN_LINE(message)

    def ShowMappingData(DItemObject, BoolType=False):
        r"""
        ## Description
        
        Show specified mapping contour on current model.
        The maximum and minimum values for this contour are automatically set. They can be modified by [Post.ResultSettings.Contour](../psj-command/post/Post.ResultSettings.Contour)_ .
        
        ## Syntax
        
        ```psj
        JPT.ShowMappingData(...)
        ```
        
        ## Inputs
        
        ### `DItemObject`
        
        - A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be display contour.
        - This is a required input.
        
        ### `BoolType`
        
        - A _Boolean_ that controls the data display type when Convection Mapping is selected.
          - _True_: Display Temperature data.
          - _False_: Display Heat Transfer Coefficient data.
        - The default value is _False_.
          
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {42}
        import os
        import csv
        import itertools
        
        def write_node_data(filename, node_data):
            headers = [
                'nodenumber', 
                'x-coordinate', 
                'y-coordinate', 
                'z-coordinate', 
                'temperature', 
                'heat-transfer-coef'
            ]
            
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)    
                writer.writerow(headers)
                for node in node_data:
                    writer.writerow(node)
        
        def generate_conv_data(
            size=5, 
            start_pos=-10, 
            step=5, 
            start_temp=-100, 
            temp_step=10, 
            start_coef=0.01, 
            coef_step=0.01
        ):
            positions = [start_pos + i * step for i in range(size)]
            nodes = [
                [i + 1, x, y, z, start_temp + i * temp_step, start_coef + i * coef_step]
                for i, (x, y, z) in enumerate(itertools.product(positions, repeat=3))
            ]
            
            return nodes
        
        def setup_mapping_view():
            JPT.DisableScreenAnimation()
            JPT.ViewFitToModel()
            conv_map = JPT.GetEntitiesByID(JPT.EntityType.LBC_MAPPING_THERMAL_CONVECTION, 1)[0]
            JPT.ShowMappingData(conv_map)
        
        def save_mapping_image(image_path):
            MainWindow.RightClick.ShowHideAllToolbar(iType=1, bShow=False)
            Home.ToImage(strImgPath=image_path)
            MainWindow.RightClick.ShowHideAllToolbar(iType=1, bShow=True)
        
        def apply_convection_mapping(csv_path):
            BoundaryConditions.Convection.SurfaceMapping(
                strName="MappingConvection_1", 
                crlTargets=[Face(24, 26, 22)], 
                iPos=2, 
                iCp=2, 
                iMappedCpIndex0=1, 
                dSearchRange=0.0, 
                iTempUnit=1, 
                strPath=csv_path
            )
        
        def main():
            temp_path = JPT.GetAppPathInfo(JPT.PathType.TEMP_PATH)
            csv_path = os.path.join(temp_path, 'node_data.csv')
            image_path = os.path.join(temp_path, "conv_img.png")
        
            #Prepare mapping data (convection)
            nodes = generate_conv_data()
            write_node_data(csv_path, nodes)
        
            #Preapre Model
            Geometry.Part.Cube(iPartColor=6409934)
            apply_convection_mapping(csv_path)
            
            #Show mapping result and save image
            setup_mapping_view()
            save_mapping_image(image_path)
        
        if __name__ == "__main__":
            main()
        ```
        
        """
        message = "JPT.ShowMappingData({},{})".format(DItemObject,BoolType)
        return JPT_RUN_LINE(message)

    def ShowMultiMappingData(DItemVector, BoolType=False):
        r"""
        ## Description
        
        Show contour of specified mapping data, including multiple data of the same type, on the current model.
        The maximum and minimum values for this contour are automatically set. They can be modified by [Post.ResultSettings.Contour](../psj-command/post/Post.ResultSettings.Contour)_ .
        
        ## Syntax
        
        ```psj
        JPT.ShowMultiMappingData(...)
        ```
        
        ## Inputs
        
        ### `DItemVector`
        
        - A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object which will be display contour.
        - This is a required input.
        
        ### `BoolType`
        
        - A _Boolean_ that controls the data display type when Convection Mapping is selected.
          - _True_: Display Temperature data.
          - _False_: Display Heat Transfer Coefficient data.
        - The default value is _False_.
          
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {42}
        import os
        import csv
        import itertools
        
        def write_node_data(filename, node_data):
            headers = [
                'nodenumber', 
                'x-coordinate', 
                'y-coordinate', 
                'z-coordinate', 
                'temperature', 
                'heat-transfer-coef'
            ]
            
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)    
                writer.writerow(headers)
                for node in node_data:
                    writer.writerow(node)
        
        def generate_conv_data(
            size=5, 
            start_pos=-10, 
            step=5, 
            start_temp=-100, 
            temp_step=10, 
            start_coef=0.01, 
            coef_step=0.01
        ):
            positions = [start_pos + i * step for i in range(size)]
            nodes = [
                [i + 1, x, y, z, start_temp + i * temp_step, start_coef + i * coef_step]
                for i, (x, y, z) in enumerate(itertools.product(positions, repeat=3))
            ]
            
            return nodes
        
        def setup_mapping_view():
            JPT.DisableScreenAnimation()
            JPT.ViewFitToModel()
            conv_maps = JPT.GetAllByTypeID(JPT.EntityType.LBC_MAPPING_THERMAL_CONVECTION)
            JPT.ShowMultiMappingData(conv_maps)
        
        def save_mapping_image(image_path):
            MainWindow.RightClick.ShowHideAllToolbar(iType=1, bShow=False)
            Home.ToImage(strImgPath=image_path)
            MainWindow.RightClick.ShowHideAllToolbar(iType=1, bShow=True)
        
        def apply_convection_mapping(csv_path):
            BoundaryConditions.Convection.SurfaceMapping(
                strName="MappingConvection_1", 
                crlTargets=[Face(24)], 
                iPos=2, 
                iCp=2, 
                iMappedCpIndex0=1, 
                dSearchRange=0.0, 
                iTempUnit=1, 
                strPath=csv_path
            )
            BoundaryConditions.Convection.SurfaceMapping(
                strName="MappingConvection_2", 
                crlTargets=[Face(26)], 
                iPos=2, 
                iCp=2, 
                iMappedCpIndex0=1, 
                dSearchRange=0.0, 
                iTempUnit=1, 
                strPath=csv_path
            )
            BoundaryConditions.Convection.SurfaceMapping(
                strName="MappingConvection_3", 
                crlTargets=[Face(22)], 
                iPos=2, 
                iCp=2, 
                iMappedCpIndex0=1, 
                dSearchRange=0.0, 
                iTempUnit=1, 
                strPath=csv_path
            )
        
        def main():
            temp_path = JPT.GetAppPathInfo(JPT.PathType.TEMP_PATH)
            csv_path = os.path.join(temp_path, 'node_data.csv')
            image_path = os.path.join(temp_path, "conv_img.png")
        
            #Prepare mapping data (convection)
            nodes = generate_conv_data()
            write_node_data(csv_path, nodes)
        
            #Preapre Model
            Geometry.Part.Cube(iPartColor=6409934)
            apply_convection_mapping(csv_path)
            
            #Show mapping result and save image
            setup_mapping_view()
            save_mapping_image(image_path)
        
        if __name__ == "__main__":
            main()
        ```
        
        """
        message = "JPT.ShowMultiMappingData({},{})".format(DItemVector,BoolType)
        return JPT_RUN_LINE(message)

    def ShowPreview():
        r"""
        ## Description
        
        Show preview render on the main screen.
        
        ## Syntax
        
        ```psj
        JPT.ShowPreview(...)
        ```
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {13}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(dlOrigin=[0.0, 0.01, 0.0], strName="Cube_2", iPartColor=13259210)
        JPT.ViewFitToModel()
        
        #Preview:
        color = JPT.ConvertRGBToJPTColor(255,255,87) #yellow
        parts = JPT.GetAllParts()
        JPT.PreviewScaling(parts,[2,1.1,1.1],[0,0,0],color,0.2)
        
        #Show Preview:
        JPT.HidePreview()
        JPT.ShowPreview()
        ```
        
        """
        message = "JPT.ShowPreview({})".format('')
        return JPT_RUN_LINE(message)

    def UpdateCheckboxAssembly(DItemType, entityID, BoolType):
        r"""
        ## Description
        
        Set the state of checkbox of item in Assembly Tree.
        
        ## Syntax
        
        ```psj
        JPT.UpdateCheckboxAssembly(DItemType, entityID, BoolType)
        ```
        
        ## Inputs
        
        ### `DItemType`
        
        - An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ of the entity.
        - This is a required input.
        
        ### `entityID`
        
        - An _Integer_ specifying the ID of the target entity.
        - This is a required input.
        
        ### `BoolType`
        
        - An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the state of checkbox:
          - _True_: Check the checkbox of item in Assembly Tree.
          - _False_: Uncheck the checkbox of item in Assembly Tree.
        - This is a required input.
        
        :::tip
        You also can input **1** instead of inputting JPT.BoolType.TRUE_VAL,
        or input **0** instead of inputting JPT.BoolType.FALSE_VAL.
        :::
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {10-11}
        # prepare model...
        JPT.Exec('CreateCube([0, 0, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube_1", 7105764, 0:0)')
        JPT.Exec('CreateCube([0.02, 0, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube_2", 6409934, 0:0)')
        JPT.Exec('CreateCube([0, 0.02, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube_3", 13259210, 0:0)')
        
        parts = JPT.GetAllParts()
        
        # update checkbox from assembly tree
        for part in parts:
            JPT.UpdateCheckboxAssembly(JPT.DItemType.BODY, part.id, 1) # turn on checkbox
            JPT.UpdateCheckboxAssembly(JPT.DItemType.BODY, part.id, 0) # turn off checkbox
        ```
        
        """
        message = "JPT.UpdateCheckboxAssembly({},{},{})".format(DItemType,entityID,BoolType)
        return JPT_RUN_LINE(message)

    def UpdateCheckboxWatchSelected(DItemType, listOfEntities, BoolType):
        r"""
        ## Description
        
        Change checkbox state ON or OFF in Watch Selected window by specifying the entity's ID and type.
        
        ## Syntax
        
        ```psj
        JPT.UpdateCheckboxWatchSelected(DItemType, listOfEntities, BoolType)
        ```
        
        ## Inputs
        
        ### `DItemType`
        
        - An _Enum_ specifying the _[DItemType](../data-type/psj-command/DItem-types)_ of the entity.
        - This is a required input.
        
        ### `listOfEntities`
        
        - A _List of Integer_ specifying the ID of the entities which will be selected or deselected.
        - This is a required input.
        
        ### `BoolType`
        
        - An _Enum_ specifying the _[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the state of checkbox:
          - _True_: Check the checkbox of item in Watch Selected window.
          - _False_: Uncheck the checkbox of item in Watch Selected window.
        - This is a required input.
        
        :::tip
        You also can input **1** instead of inputting JPT.BoolType.TRUE_VAL,
        or input **0** instead of inputting JPT.BoolType.FALSE_VAL.
        :::
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {139-145}
        # Prepare model
        Geometry.Part.Cube()
        Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                           strName="Cube_2",
                           iPartColor=6409934)
        Geometry.Part.Cube(dlOrigin=[0.02, 0.0, 0.0],
                           strName="Cube_3",
                           iPartColor=13259210)
        Geometry.Part.Cube(dlOrigin=[0.03, 0.0, 0.0],
                           strName="Cube_4",
                           iPartColor=7697908)
        Geometry.Part.Cube(dlOrigin=[0.04, 0.0, 0.0],
                           strName="Cube_5",
                           iPartColor=7463537)
        Geometry.Part.Cube(dlOrigin=[0.05, 0.0, 0.0],
                           strName="Cube_6",
                           iPartColor=7434735)
        Geometry.Part.Cube(dlOrigin=[0.06, 0.0, 0.0],
                           strName="Cube_7",
                           iPartColor=14903267)
        Geometry.Part.Cube(dlOrigin=[0.07, 0.0, 0.0],
                           strName="Cube_8",
                           iPartColor=15658599)
        JPT.ViewFitToModel()
        
        # Renumber Node ID & Element ID
        Tools.Renumber(listRenumberItem=[RENUMBER_ITEM(crTarget=Part(1),
                                                       iBeginID=1,
                                                       iCount=488,
                                                       ilOffset=[10000, 100, 1],
                                                       dlCoordTolerance=[0.1, 0.1, 0.1],
                                                       bEnable=True),
                                         RENUMBER_ITEM(crTarget=Part(2),
                                                       iBeginID=489,
                                                       iCount=488,
                                                       ilOffset=[10000, 100, 1],
                                                       dlCoordTolerance=[0.1, 0.1, 0.1],
                                                       bEnable=True),
                                         RENUMBER_ITEM(crTarget=Part(3),
                                                       iBeginID=977,
                                                       iCount=488,
                                                       ilOffset=[10000, 100, 1],
                                                       dlCoordTolerance=[0.1, 0.1, 0.1],
                                                       bEnable=True),
                                         RENUMBER_ITEM(crTarget=Part(4),
                                                       iBeginID=1465,
                                                       iCount=488,
                                                       ilOffset=[10000, 100, 1],
                                                       dlCoordTolerance=[0.1, 0.1, 0.1],
                                                       bEnable=True),
                                         RENUMBER_ITEM(crTarget=Part(5),
                                                       iBeginID=1953,
                                                       iCount=488,
                                                       ilOffset=[10000, 100, 1],
                                                       dlCoordTolerance=[0.1, 0.1, 0.1],
                                                       bEnable=True),
                                         RENUMBER_ITEM(crTarget=Part(6),
                                                       iBeginID=2441,
                                                       iCount=488,
                                                       ilOffset=[10000, 100, 1],
                                                       dlCoordTolerance=[0.1, 0.1, 0.1],
                                                       bEnable=True),
                                         RENUMBER_ITEM(crTarget=Part(7),
                                                       iBeginID=2929,
                                                       iCount=488,
                                                       ilOffset=[10000, 100, 1],
                                                       dlCoordTolerance=[0.1, 0.1, 0.1],
                                                       bEnable=True),
                                         RENUMBER_ITEM(crTarget=Part(8),
                                                       iBeginID=3417,
                                                       iCount=488,
                                                       ilOffset=[10000, 100, 1],
                                                       dlCoordTolerance=[0.1, 0.1, 0.1],
                                                       bEnable=True)])
        Tools.Renumber(listRenumberItem=[RENUMBER_ITEM(crTarget=Part(1),
                                                       iBeginID=1,
                                                       iTargetType=2,
                                                       iCount=972,
                                                       ilOffset=[10000, 100, 1],
                                                       dlCoordTolerance=[0.1, 0.1, 0.1],
                                                       bEnable=True),
                                         RENUMBER_ITEM(crTarget=Part(2),
                                                       iBeginID=973,
                                                       iTargetType=2,
                                                       iCount=972,
                                                       ilOffset=[10000, 100, 1],
                                                       dlCoordTolerance=[0.1, 0.1, 0.1],
                                                       bEnable=True),
                                         RENUMBER_ITEM(crTarget=Part(3),
                                                       iBeginID=1945, iTargetType=2,
                                                       iCount=972,
                                                       ilOffset=[10000, 100, 1],
                                                       dlCoordTolerance=[0.1, 0.1, 0.1],
                                                       bEnable=True),
                                         RENUMBER_ITEM(crTarget=Part(4),
                                                       iBeginID=2917,
                                                       iTargetType=2,
                                                       iCount=972,
                                                       ilOffset=[10000, 100, 1],
                                                       dlCoordTolerance=[0.1, 0.1, 0.1],
                                                       bEnable=True),
                                         RENUMBER_ITEM(crTarget=Part(5),
                                                       iBeginID=3889,
                                                       iTargetType=2,
                                                       iCount=972,
                                                       ilOffset=[10000, 100, 1],
                                                       dlCoordTolerance=[0.1, 0.1, 0.1],
                                                       bEnable=True),
                                         RENUMBER_ITEM(crTarget=Part(6),
                                                       iBeginID=4861,
                                                       iTargetType=2,
                                                       iCount=972,
                                                       ilOffset=[10000, 100, 1],
                                                       dlCoordTolerance=[0.1, 0.1, 0.1],
                                                       bEnable=True),
                                         RENUMBER_ITEM(crTarget=Part(7),
                                                       iBeginID=5833,
                                                       iTargetType=2,
                                                       iCount=972,
                                                       ilOffset=[10000, 100, 1],
                                                       dlCoordTolerance=[0.1, 0.1, 0.1],
                                                       bEnable=True),
                                         RENUMBER_ITEM(crTarget=Part(8),
                                                       iBeginID=6805,
                                                       iTargetType=2,
                                                       iCount=972,
                                                       ilOffset=[10000, 100, 1],
                                                       dlCoordTolerance=[0.1, 0.1, 0.1],
                                                       bEnable=True)],
                       bAssignProp=False)
        
        # Find entities
        Home.Find(strSearch="1 2 3 4 5",
                  strSelectedType="Node")
        Home.Find(strSearch="1 2 3 4 5",
                  strSelectedType="2D Element")
        
        # Change checkbox state in Watch Selected window
        JPT.UpdateCheckboxWatchSelected(JPT.DItemType.NODE,
                                        [1, 2, 3],
                                        JPT.BoolType.FALSE_VAL)
        JPT.UpdateCheckboxWatchSelected(JPT.DItemType.ELEM,
                                        [1, 2, 3],
                                        JPT.BoolType.FALSE_VAL)
        ```
        
        """
        message = "JPT.UpdateCheckboxWatchSelected({},{},{})".format(DItemType,listOfEntities,BoolType)
        return JPT_RUN_LINE(message)

    def ViewFitToModel():
        r"""
        ## Description
        
        Change the view of the current model to fit with the Jupiter display window.
        
        ## Syntax
        
        ```psj
        JPT.ViewFitToModel()
        ```
        Macro: [ViewFitToModel](../../macro/view-control/ViewFitToModel)
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {1}
        JPT.ViewFitToModel()
        ```
        
        """
        message = "JPT.ViewFitToModel({})".format('')
        return JPT_RUN_LINE(message)

    def ViewNormalDisplay():
        r"""
        ## Description
        
        Back to the Normal Display.
        
        ## Syntax
        
        ```psj
        JPT.ViewNormalDisplay()
        ```
        
        Macro: [ViewNormalDisplay](../../macro/view-control/ViewNormalDisplay)
        
        ## Inputs
        
        This utility function does not require any input value.
        
        ## Return Code
        
        This utility function does not have output value.
        
        ## Sample Code
        
        ```psj {1}
        JPT.ViewNormalDisplay()
        ```
        
        """
        message = "JPT.ViewNormalDisplay({})".format('')
        return JPT_RUN_LINE(message)

