from enum import Enum
from typing import Any, Dict, Tuple
from bitstring import BitStream

class InputAction(Enum):
    Nothing = 0
    StopWalking = 1
    BeginMining = 2
    StopMining = 3
    ToggleDriving = 4
    OpenGui = 5
    CloseGui = 6
    OpenCharacterGui = 7
    OpenCurrentVehicleGui = 8
    ConnectRollingStock = 9
    DisconnectRollingStock = 10
    SelectedEntityCleared = 11
    ClearCursor = 12
    ResetAssemblingMachine = 13
    OpenTechnologyGui = 14
    LaunchRocket = 15
    OpenProductionGui = 16
    StopRepair = 17
    CancelNewBlueprint = 18
    CloseBlueprintRecord = 19
    CopyEntitySettings = 20
    PasteEntitySettings = 21
    DestroyOpenedItem = 22
    CopyOpenedItem = 23
    ToggleShowEntityInfo = 24
    SingleplayerInit = 25
    MultiplayerInit = 26
    DisconnectAllPlayers = 27
    SwitchToRenameStopGui = 28
    OpenBonusGui = 29
    OpenTrainsGui = 30
    OpenAchievementsGui = 31
    CycleBlueprintBookForwards = 32
    CycleBlueprintBookBackwards = 33
    CycleClipboardForwards = 34
    CycleClipboardBackwards = 35
    StopMovementInTheNextTick = 36
    ToggleEnableVehicleLogisticsWhileMoving = 37
    ToggleDeconstructionItemEntityFilterMode = 38
    ToggleDeconstructionItemTileFilterMode = 39
    OpenLogisticGui = 40
    SelectNextValidGun = 41
    ToggleMapEditor = 42
    DeleteBlueprintLibrary = 43
    GameCreatedFromScenario = 44
    ActivateCopy = 45
    ActivateCut = 46
    ActivatePaste = 47
    Undo = 48
    TogglePersonalRoboport = 49
    ToggleEquipmentMovementBonus = 50
    TogglePersonalLogisticRequests = 51
    ToggleEntityLogisticRequests = 52
    StopBuildingByMoving = 53
    FlushOpenedEntityFluid = 54
    ForceFullCRC = 55
    OpenTipsAndTricksGui = 56
    OpenBlueprintLibraryGui = 57
    ChangeBlueprintLibraryTab = 58
    DropItem = 59
    Build = 60
    StartWalking = 61
    BeginMiningTerrain = 62
    ChangeRidingState = 63
    OpenItem = 64
    OpenParentOfOpenedItem = 65
    ResetItem = 66
    DestroyItem = 67
    OpenModItem = 68
    OpenEquipment = 69
    CursorTransfer = 70
    CursorSplit = 71
    StackTransfer = 72
    InventoryTransfer = 73
    CheckCRCHeuristic = 74
    Craft = 75
    WireDragging = 76
    ChangeShootingState = 77
    SetupAssemblingMachine = 78
    SelectedEntityChanged = 79
    SmartPipette = 80
    StackSplit = 81
    InventorySplit = 82
    CancelCraft = 83
    SetFilter = 84
    CheckCRC = 85
    SetCircuitCondition = 86
    SetSignal = 87
    StartResearch = 88
    SetLogisticFilterItem = 89
    SetLogisticFilterSignal = 90
    SetCircuitModeOfOperation = 91
    GuiClick = 92
    GuiConfirmed = 93
    WriteToConsole = 94
    MarketOffer = 95
    AddTrainStation = 96
    ChangeTrainStopStation = 97
    ChangeActiveItemGroupForCrafting = 98
    ChangeActiveItemGroupForFilters = 99
    ChangeActiveCharacterTab = 100
    GuiTextChanged = 101
    GuiCheckedStateChanged = 102
    GuiSelectionStateChanged = 103
    GuiSelectedTabChanged = 104
    GuiValueChanged = 105
    GuiSwitchStateChanged = 106
    GuiLocationChanged = 107
    PlaceEquipment = 108
    TakeEquipment = 109
    UseItem = 110
    SendSpidertron = 111
    UseArtilleryRemote = 112
    SetInventoryBar = 113
    MoveOnZoom = 114
    StartRepair = 115
    Deconstruct = 116
    Upgrade = 117
    Copy = 118
    AlternativeCopy = 119
    SelectBlueprintEntities = 120
    AltSelectBlueprintEntities = 121
    SetupBlueprint = 122
    SetupSingleBlueprintRecord = 123
    CopyOpenedBlueprint = 124
    ReassignBlueprint = 125
    OpenBlueprintRecord = 126
    GrabBlueprintRecord = 127
    DropBlueprintRecord = 128
    DeleteBlueprintRecord = 129
    UpgradeOpenedBlueprintByRecord = 130
    UpgradeOpenedBlueprintByItem = 131
    SpawnItem = 132
    SpawnItemStackTransfer = 133
    UpdateBlueprintShelf = 134
    TransferBlueprint = 135
    TransferBlueprintImmediately = 136
    EditBlueprintToolPreview = 137
    RemoveCables = 138
    ExportBlueprint = 139
    ImportBlueprint = 140
    ImportBlueprintsFiltered = 141
    PlayerJoinGame = 142
    PlayerAdminChange = 143
    CancelDeconstruct = 144
    CancelUpgrade = 145
    ChangeArithmeticCombinatorParameters = 146
    ChangeDeciderCombinatorParameters = 147
    ChangeProgrammableSpeakerParameters = 148
    ChangeProgrammableSpeakerAlertParameters = 149
    ChangeProgrammableSpeakerCircuitParameters = 150
    SetVehicleAutomaticTargetingParameters = 151
    BuildTerrain = 152
    ChangeTrainWaitCondition = 153
    ChangeTrainWaitConditionData = 154
    CustomInput = 155
    ChangeItemLabel = 156
    ChangeItemDescription = 157
    ChangeEntityLabel = 158
    BuildRail = 159
    CancelResearch = 160
    SelectArea = 161
    AltSelectArea = 162
    ReverseSelectArea = 163
    AltReverseSelectArea = 164
    ServerCommand = 165
    SetControllerLogisticTrashFilterItem = 166
    SetEntityLogisticTrashFilterItem = 167
    SetInfinityContainerFilterItem = 168
    SetInfinityPipeFilter = 169
    ModSettingsChanged = 170
    SetEntityEnergyProperty = 171
    EditCustomTag = 172
    EditPermissionGroup = 173
    ImportBlueprintString = 174
    ImportPermissionsString = 175
    ReloadScript = 176
    ReloadScriptDataTooLarge = 177
    GuiElemChanged = 178
    BlueprintTransferQueueUpdate = 179
    DragTrainSchedule = 180
    DragTrainWaitCondition = 181
    SelectItem = 182
    SelectEntitySlot = 183
    SelectTileSlot = 184
    SelectMapperSlot = 185
    DisplayResolutionChanged = 186
    QuickBarSetSlot = 187
    QuickBarPickSlot = 188
    QuickBarSetSelectedPage = 189
    PlayerLeaveGame = 190
    MapEditorAction = 191
    PutSpecialItemInMap = 192
    PutSpecialRecordInMap = 193
    ChangeMultiplayerConfig = 194
    AdminAction = 195
    LuaShortcut = 196
    TranslateString = 197
    FlushOpenedEntitySpecificFluid = 198
    ChangePickingState = 199
    SelectedEntityChangedVeryClose = 200
    SelectedEntityChangedVeryClosePrecise = 201
    SelectedEntityChangedRelative = 202
    SelectedEntityChangedBasedOnUnitNumber = 203
    SetAutosortInventory = 204
    SetFlatControllerGui = 205
    SetRecipeNotifications = 206
    SetAutoLaunchRocket = 207
    SwitchConstantCombinatorState = 208
    SwitchPowerSwitchState = 209
    SwitchInserterFilterModeState = 210
    SwitchConnectToLogisticNetwork = 211
    SetBehaviorMode = 212
    FastEntityTransfer = 213
    RotateEntity = 214
    FastEntitySplit = 215
    SetTrainStopped = 216
    ChangeControllerSpeed = 217
    SetAllowCommands  = 218
    SetResearchFinishedStopsGame = 219
    SetInserterMaxStackSize = 220
    OpenTrainGui = 221
    SetEntityColor = 222
    SetDeconstructionItemTreesAndRocksOnly = 223
    SetDeconstructionItemTileSelectionMode = 224
    DeleteCustomTag = 225
    DeletePermissionGroup = 226
    AddPermissionGroup = 227
    SetInfinityContainerRemoveUnfilteredItems = 228
    SetCarWeaponsControl = 229
    SetRequestFromBuffers = 230
    ChangeActiveQuickBar = 231
    OpenPermissionsGui = 232
    DisplayScaleChanged = 233
    SetSplitterPriority = 234
    GrabInternalBlueprintFromText = 235
    SetHeatInterfaceTemperature = 236
    SetHeatInterfaceMode = 237
    OpenTrainStationGui = 238
    RemoveTrainStation = 239
    GoToTrainStation = 240
    RenderModeChanged = 241
    PlayerInputMethodChanged = 242
    SetPlayerColor = 243
    PlayerClickedGpsTag = 244
    SetTrainsLimit = 245
    ClearRecipeNotification = 246
    SetLinkedContainerLinkID = 247
    GuiHover = 248
    GuiLeave = 249


def decode_check_crc_heuristic(payload: BitStream) -> Tuple[Dict[str, Any], BitStream]:
    crc, tick_of_crc = payload.readlist("uintle32, uintle32")

    return {"crc": crc, "tick_of_crc": tick_of_crc}, payload[payload.pos:]

INPUT_ACTION_LOOKUP_TABLE = {
    InputAction.Nothing                                         : {"index":   0, "length":     0, "decoder": None},
    InputAction.StopWalking                                     : {"index":   1, "length":     0, "decoder": None},
    InputAction.BeginMining                                     : {"index":   2, "length":     0, "decoder": None},
    InputAction.StopMining                                      : {"index":   3, "length":     0, "decoder": None},
    InputAction.ToggleDriving                                   : {"index":   4, "length":     0, "decoder": None},
    InputAction.OpenGui                                         : {"index":   5, "length":     0, "decoder": None},
    InputAction.CloseGui                                        : {"index":   6, "length":     0, "decoder": None},
    InputAction.OpenCharacterGui                                : {"index":   7, "length":     0, "decoder": None},
    InputAction.OpenCurrentVehicleGui                           : {"index":   8, "length":     0, "decoder": None},
    InputAction.ConnectRollingStock                             : {"index":   9, "length":     0, "decoder": None},
    InputAction.DisconnectRollingStock                          : {"index":  10, "length":     0, "decoder": None},
    InputAction.SelectedEntityCleared                           : {"index":  11, "length":     0, "decoder": None},
    InputAction.ClearCursor                                     : {"index":  12, "length":     0, "decoder": None},
    InputAction.ResetAssemblingMachine                          : {"index":  13, "length":     0, "decoder": None},
    InputAction.OpenTechnologyGui                               : {"index":  14, "length":     0, "decoder": None},
    InputAction.LaunchRocket                                    : {"index":  15, "length":     0, "decoder": None},
    InputAction.OpenProductionGui                               : {"index":  16, "length":     0, "decoder": None},
    InputAction.StopRepair                                      : {"index":  17, "length":     0, "decoder": None},
    InputAction.CancelNewBlueprint                              : {"index":  18, "length":     0, "decoder": None},
    InputAction.CloseBlueprintRecord                            : {"index":  19, "length":     0, "decoder": None},
    InputAction.CopyEntitySettings                              : {"index":  20, "length":     0, "decoder": None},
    InputAction.PasteEntitySettings                             : {"index":  21, "length":     0, "decoder": None},
    InputAction.DestroyOpenedItem                               : {"index":  22, "length":     0, "decoder": None},
    InputAction.CopyOpenedItem                                  : {"index":  23, "length":     0, "decoder": None},
    InputAction.ToggleShowEntityInfo                            : {"index":  24, "length":     0, "decoder": None},
    InputAction.SingleplayerInit                                : {"index":  25, "length":     0, "decoder": None},
    InputAction.MultiplayerInit                                 : {"index":  26, "length":     0, "decoder": None},
    InputAction.DisconnectAllPlayers                            : {"index":  27, "length":     0, "decoder": None},
    InputAction.SwitchToRenameStopGui                           : {"index":  28, "length":     0, "decoder": None},
    InputAction.OpenBonusGui                                    : {"index":  29, "length":     0, "decoder": None},
    InputAction.OpenTrainsGui                                   : {"index":  30, "length":     0, "decoder": None},
    InputAction.OpenAchievementsGui                             : {"index":  31, "length":     0, "decoder": None},
    InputAction.CycleBlueprintBookForwards                      : {"index":  32, "length":     0, "decoder": None},
    InputAction.CycleBlueprintBookBackwards                     : {"index":  33, "length":     0, "decoder": None},
    InputAction.CycleClipboardForwards                          : {"index":  34, "length":     0, "decoder": None},
    InputAction.CycleClipboardBackwards                         : {"index":  35, "length":     0, "decoder": None},
    InputAction.StopMovementInTheNextTick                       : {"index":  36, "length":     0, "decoder": None},
    InputAction.ToggleEnableVehicleLogisticsWhileMoving         : {"index":  37, "length":     0, "decoder": None},
    InputAction.ToggleDeconstructionItemEntityFilterMode        : {"index":  38, "length":     0, "decoder": None},
    InputAction.ToggleDeconstructionItemTileFilterMode          : {"index":  39, "length":     0, "decoder": None},
    InputAction.OpenLogisticGui                                 : {"index":  40, "length":     0, "decoder": None},
    InputAction.SelectNextValidGun                              : {"index":  41, "length":     0, "decoder": None},
    InputAction.ToggleMapEditor                                 : {"index":  42, "length":     0, "decoder": None},
    InputAction.DeleteBlueprintLibrary                          : {"index":  43, "length":     0, "decoder": None},
    InputAction.GameCreatedFromScenario                         : {"index":  44, "length":     0, "decoder": None},
    InputAction.ActivateCopy                                    : {"index":  45, "length":     0, "decoder": None},
    InputAction.ActivateCut                                     : {"index":  46, "length":     0, "decoder": None},
    InputAction.ActivatePaste                                   : {"index":  47, "length":     0, "decoder": None},
    InputAction.Undo                                            : {"index":  48, "length":     0, "decoder": None},
    InputAction.TogglePersonalRoboport                          : {"index":  49, "length":     0, "decoder": None},
    InputAction.ToggleEquipmentMovementBonus                    : {"index":  50, "length":     0, "decoder": None},
    InputAction.TogglePersonalLogisticRequests                  : {"index":  51, "length":     0, "decoder": None},
    InputAction.ToggleEntityLogisticRequests                    : {"index":  52, "length":     0, "decoder": None},
    InputAction.StopBuildingByMoving                            : {"index":  53, "length":     0, "decoder": None},
    InputAction.FlushOpenedEntityFluid                          : {"index":  54, "length":     0, "decoder": None},
    InputAction.ForceFullCRC                                    : {"index":  55, "length":     0, "decoder": None},
    InputAction.OpenTipsAndTricksGui                            : {"index":  56, "length":     4, "decoder": None},
    InputAction.OpenBlueprintLibraryGui                         : {"index":  57, "length":     2, "decoder": None},
    InputAction.ChangeBlueprintLibraryTab                       : {"index":  58, "length":     3, "decoder": None},
    InputAction.DropItem                                        : {"index":  59, "length":     8, "decoder": None},
    InputAction.Build                                           : {"index":  60, "length":     5, "decoder": None},
    InputAction.StartWalking                                    : {"index":  61, "length":     1, "decoder": None},
    InputAction.BeginMiningTerrain                              : {"index":  62, "length":     8, "decoder": None},
    InputAction.ChangeRidingState                               : {"index":  63, "length":     2, "decoder": None},
    InputAction.OpenItem                                        : {"index":  64, "length":     5, "decoder": None},
    InputAction.OpenParentOfOpenedItem                          : {"index":  65, "length":     2, "decoder": None},
    InputAction.ResetItem                                       : {"index":  66, "length":     5, "decoder": None},
    InputAction.DestroyItem                                     : {"index":  67, "length":     8, "decoder": None},
    InputAction.OpenModItem                                     : {"index":  68, "length":     6, "decoder": None},
    InputAction.OpenEquipment                                   : {"index":  69, "length":  None, "decoder": None},
    InputAction.CursorTransfer                                  : {"index":  70, "length":     9, "decoder": None},
    InputAction.CursorSplit                                     : {"index":  71, "length":     5, "decoder": None},
    InputAction.StackTransfer                                   : {"index":  72, "length":     5, "decoder": None},
    InputAction.InventoryTransfer                               : {"index":  73, "length":     5, "decoder": None},
    InputAction.CheckCRCHeuristic                               : {"index":  74, "length":    11, "decoder": decode_check_crc_heuristic},
    InputAction.Craft                                           : {"index":  75, "length":     5, "decoder": None},
    InputAction.WireDragging                                    : {"index":  76, "length":     8, "decoder": None},
    InputAction.ChangeShootingState                             : {"index":  77, "length":     9, "decoder": None},
    InputAction.SetupAssemblingMachine                          : {"index":  78, "length":  None, "decoder": None},
    InputAction.SelectedEntityChanged                           : {"index":  79, "length":     8, "decoder": None},
    InputAction.SmartPipette                                    : {"index":  80, "length":  None, "decoder": None},
    InputAction.StackSplit                                      : {"index":  81, "length":     2, "decoder": None},
    InputAction.InventorySplit                                  : {"index":  82, "length":     8, "decoder": None},
    InputAction.CancelCraft                                     : {"index":  83, "length":  None, "decoder": None},
    InputAction.SetFilter                                       : {"index":  84, "length":  None, "decoder": None},
    InputAction.CheckCRC                                        : {"index":  85, "length":     9, "decoder": None},
    InputAction.SetCircuitCondition                             : {"index":  86, "length":  None, "decoder": None},
    InputAction.SetSignal                                       : {"index":  87, "length":  None, "decoder": None},
    InputAction.StartResearch                                   : {"index":  88, "length":  None, "decoder": None},
    InputAction.SetLogisticFilterItem                           : {"index":  89, "length":  None, "decoder": None},
    InputAction.SetLogisticFilterSignal                         : {"index":  90, "length":     1, "decoder": None},
    InputAction.SetCircuitModeOfOperation                       : {"index":  91, "length":    12, "decoder": None},
    InputAction.GuiClick                                        : {"index":  92, "length":  None, "decoder": None},
    InputAction.GuiConfirmed                                    : {"index":  93, "length":  None, "decoder": None},
    InputAction.WriteToConsole                                  : {"index":  94, "length":  None, "decoder": None},
    InputAction.MarketOffer                                     : {"index":  95, "length":     9, "decoder": None},
    InputAction.AddTrainStation                                 : {"index":  96, "length":     9, "decoder": None},
    InputAction.ChangeTrainStopStation                          : {"index":  97, "length":  None, "decoder": None},
    InputAction.ChangeActiveItemGroupForCrafting                : {"index":  98, "length":    25, "decoder": None},
    InputAction.ChangeActiveItemGroupForFilters                 : {"index":  99, "length":     5, "decoder": None},
    InputAction.ChangeActiveCharacterTab                        : {"index": 100, "length":     1, "decoder": None},
    InputAction.GuiTextChanged                                  : {"index": 101, "length":  None, "decoder": None},
    InputAction.GuiCheckedStateChanged                          : {"index": 102, "length":     8, "decoder": None},
    InputAction.GuiSelectionStateChanged                        : {"index": 103, "length":  None, "decoder": None},
    InputAction.GuiSelectedTabChanged                           : {"index": 104, "length":  None, "decoder": None},
    InputAction.GuiValueChanged                                 : {"index": 105, "length":    23, "decoder": None},
    InputAction.GuiSwitchStateChanged                           : {"index": 106, "length":  None, "decoder": None},
    InputAction.GuiLocationChanged                              : {"index": 107, "length":    23, "decoder": None},
    InputAction.PlaceEquipment                                  : {"index": 108, "length":  None, "decoder": None},
    InputAction.TakeEquipment                                   : {"index": 109, "length":  None, "decoder": None},
    InputAction.UseItem                                         : {"index": 110, "length":     8, "decoder": None},
    InputAction.SendSpidertron                                  : {"index": 111, "length":  None, "decoder": None},
    InputAction.UseArtilleryRemote                              : {"index": 112, "length":     8, "decoder": None},
    InputAction.SetInventoryBar                                 : {"index": 113, "length":     6, "decoder": None},
    InputAction.MoveOnZoom                                      : {"index": 114, "length":  None, "decoder": None},
    InputAction.StartRepair                                     : {"index": 115, "length":     8, "decoder": None},
    InputAction.Deconstruct                                     : {"index": 116, "length":     8, "decoder": None},
    InputAction.Upgrade                                         : {"index": 117, "length":  None, "decoder": None},
    InputAction.Copy                                            : {"index": 118, "length":     2, "decoder": None},
    InputAction.AlternativeCopy                                 : {"index": 119, "length":  None, "decoder": None},
    InputAction.SelectBlueprintEntities                         : {"index": 120, "length":  None, "decoder": None},
    InputAction.AltSelectBlueprintEntities                      : {"index": 121, "length":  None, "decoder": None},
    InputAction.SetupBlueprint                                  : {"index": 122, "length":  None, "decoder": None},
    InputAction.SetupSingleBlueprintRecord                      : {"index": 123, "length":  None, "decoder": None},
    InputAction.CopyOpenedBlueprint                             : {"index": 124, "length":  None, "decoder": None},
    InputAction.ReassignBlueprint                               : {"index": 125, "length":  None, "decoder": None},
    InputAction.OpenBlueprintRecord                             : {"index": 126, "length":  None, "decoder": None},
    InputAction.GrabBlueprintRecord                             : {"index": 127, "length":  None, "decoder": None},
    InputAction.DropBlueprintRecord                             : {"index": 128, "length":  None, "decoder": None},
    InputAction.DeleteBlueprintRecord                           : {"index": 129, "length":  None, "decoder": None},
    InputAction.UpgradeOpenedBlueprintByRecord                  : {"index": 130, "length":  None, "decoder": None},
    InputAction.UpgradeOpenedBlueprintByItem                    : {"index": 131, "length":  None, "decoder": None},
    InputAction.SpawnItem                                       : {"index": 132, "length":  None, "decoder": None},
    InputAction.SpawnItemStackTransfer                          : {"index": 133, "length":  None, "decoder": None},
    InputAction.UpdateBlueprintShelf                            : {"index": 134, "length":  None, "decoder": None},
    InputAction.TransferBlueprint                               : {"index": 135, "length":    13, "decoder": None},
    InputAction.TransferBlueprintImmediately                    : {"index": 136, "length":    10, "decoder": None},
    InputAction.EditBlueprintToolPreview                        : {"index": 137, "length":  None, "decoder": None},
    InputAction.RemoveCables                                    : {"index": 138, "length":     8, "decoder": None},
    InputAction.ExportBlueprint                                 : {"index": 139, "length":  None, "decoder": None},
    InputAction.ImportBlueprint                                 : {"index": 140, "length":    16, "decoder": None},
    InputAction.ImportBlueprintsFiltered                        : {"index": 141, "length":     6, "decoder": None},
    InputAction.PlayerJoinGame                                  : {"index": 142, "length":  None, "decoder": None},
    InputAction.PlayerAdminChange                               : {"index": 143, "length":     1, "decoder": None},
    InputAction.CancelDeconstruct                               : {"index": 144, "length":  None, "decoder": None},
    InputAction.CancelUpgrade                                   : {"index": 145, "length":     5, "decoder": None},
    InputAction.ChangeArithmeticCombinatorParameters            : {"index": 146, "length":  None, "decoder": None},
    InputAction.ChangeDeciderCombinatorParameters               : {"index": 147, "length":  None, "decoder": None},
    InputAction.ChangeProgrammableSpeakerParameters             : {"index": 148, "length":  None, "decoder": None},
    InputAction.ChangeProgrammableSpeakerAlertParameters        : {"index": 149, "length":  None, "decoder": None},
    InputAction.ChangeProgrammableSpeakerCircuitParameters      : {"index": 150, "length":  None, "decoder": None},
    InputAction.SetVehicleAutomaticTargetingParameters          : {"index": 151, "length":  None, "decoder": None},
    InputAction.BuildTerrain                                    : {"index": 152, "length":  None, "decoder": None},
    InputAction.ChangeTrainWaitCondition                        : {"index": 153, "length":  None, "decoder": None},
    InputAction.ChangeTrainWaitConditionData                    : {"index": 154, "length":  None, "decoder": None},
    InputAction.CustomInput                                     : {"index": 155, "length":  None, "decoder": None},
    InputAction.ChangeItemLabel                                 : {"index": 156, "length":  None, "decoder": None},
    InputAction.ChangeItemDescription                           : {"index": 157, "length":  None, "decoder": None},
    InputAction.ChangeEntityLabel                               : {"index": 158, "length":  None, "decoder": None},
    InputAction.BuildRail                                       : {"index": 159, "length":  None, "decoder": None},
    InputAction.CancelResearch                                  : {"index": 160, "length":    12, "decoder": None},
    InputAction.SelectArea                                      : {"index": 161, "length":  None, "decoder": None},
    InputAction.AltSelectArea                                   : {"index": 162, "length":  None, "decoder": None},
    InputAction.ReverseSelectArea                               : {"index": 163, "length":  None, "decoder": None},
    InputAction.AltReverseSelectArea                            : {"index": 164, "length":  None, "decoder": None},
    InputAction.ServerCommand                                   : {"index": 165, "length":     4, "decoder": None},
    InputAction.SetControllerLogisticTrashFilterItem            : {"index": 166, "length":  None, "decoder": None},
    InputAction.SetEntityLogisticTrashFilterItem                : {"index": 167, "length":  None, "decoder": None},
    InputAction.SetInfinityContainerFilterItem                  : {"index": 168, "length":  None, "decoder": None},
    InputAction.SetInfinityPipeFilter                           : {"index": 169, "length":     8, "decoder": None},
    InputAction.ModSettingsChanged                              : {"index": 170, "length":     7, "decoder": None},
    InputAction.SetEntityEnergyProperty                         : {"index": 171, "length":     4, "decoder": None},
    InputAction.EditCustomTag                                   : {"index": 172, "length":     2, "decoder": None},
    InputAction.EditPermissionGroup                             : {"index": 173, "length":     1, "decoder": None},
    InputAction.ImportBlueprintString                           : {"index": 174, "length":  None, "decoder": None},
    InputAction.ImportPermissionsString                         : {"index": 175, "length":  None, "decoder": None},
    InputAction.ReloadScript                                    : {"index": 176, "length":  None, "decoder": None},
    InputAction.ReloadScriptDataTooLarge                        : {"index": 177, "length":  None, "decoder": None},
    InputAction.GuiElemChanged                                  : {"index": 178, "length":  None, "decoder": None},
    InputAction.BlueprintTransferQueueUpdate                    : {"index": 179, "length":     1, "decoder": None},
    InputAction.DragTrainSchedule                               : {"index": 180, "length":     1, "decoder": None},
    InputAction.DragTrainWaitCondition                          : {"index": 181, "length":     2, "decoder": None},
    InputAction.SelectItem                                      : {"index": 182, "length":     4, "decoder": None},
    InputAction.SelectEntitySlot                                : {"index": 183, "length":     4, "decoder": None},
    InputAction.SelectTileSlot                                  : {"index": 184, "length":  None, "decoder": None},
    InputAction.SelectMapperSlot                                : {"index": 185, "length":  None, "decoder": None},
    InputAction.DisplayResolutionChanged                        : {"index": 186, "length":  None, "decoder": None},
    InputAction.QuickBarSetSlot                                 : {"index": 187, "length":  None, "decoder": None},
    InputAction.QuickBarPickSlot                                : {"index": 188, "length":  None, "decoder": None},
    InputAction.QuickBarSetSelectedPage                         : {"index": 189, "length":  None, "decoder": None},
    InputAction.PlayerLeaveGame                                 : {"index": 190, "length":     1, "decoder": None},
    InputAction.MapEditorAction                                 : {"index": 191, "length":     1, "decoder": None},
    InputAction.PutSpecialItemInMap                             : {"index": 192, "length":     1, "decoder": None},
    InputAction.PutSpecialRecordInMap                           : {"index": 193, "length":     1, "decoder": None},
    InputAction.ChangeMultiplayerConfig                         : {"index": 194, "length":     1, "decoder": None},
    InputAction.AdminAction                                     : {"index": 195, "length":  None, "decoder": None},
    InputAction.LuaShortcut                                     : {"index": 196, "length":  None, "decoder": None},
    InputAction.TranslateString                                 : {"index": 197, "length":  None, "decoder": None},
    InputAction.FlushOpenedEntitySpecificFluid                  : {"index": 198, "length":  None, "decoder": None},
    InputAction.ChangePickingState                              : {"index": 199, "length":     1, "decoder": None},
    InputAction.SelectedEntityChangedVeryClose                  : {"index": 200, "length":     1, "decoder": None},
    InputAction.SelectedEntityChangedVeryClosePrecise           : {"index": 201, "length":     2, "decoder": None},
    InputAction.SelectedEntityChangedRelative                   : {"index": 202, "length":     4, "decoder": None},
    InputAction.SelectedEntityChangedBasedOnUnitNumber          : {"index": 203, "length":     4, "decoder": None},
    InputAction.SetAutosortInventory                            : {"index": 204, "length":     1, "decoder": None},
    InputAction.SetFlatControllerGui                            : {"index": 205, "length":     1, "decoder": None},
    InputAction.SetRecipeNotifications                          : {"index": 206, "length":     1, "decoder": None},
    InputAction.SetAutoLaunchRocket                             : {"index": 207, "length":     2, "decoder": None},
    InputAction.SwitchConstantCombinatorState                   : {"index": 208, "length":     1, "decoder": None},
    InputAction.SwitchPowerSwitchState                          : {"index": 209, "length":     1, "decoder": None},
    InputAction.SwitchInserterFilterModeState                   : {"index": 210, "length":     1, "decoder": None},
    InputAction.SwitchConnectToLogisticNetwork                  : {"index": 211, "length":     1, "decoder": None},
    InputAction.SetBehaviorMode                                 : {"index": 212, "length":     1, "decoder": None},
    InputAction.FastEntityTransfer                              : {"index": 213, "length":     1, "decoder": None},
    InputAction.RotateEntity                                    : {"index": 214, "length":     1, "decoder": None},
    InputAction.FastEntitySplit                                 : {"index": 215, "length":     1, "decoder": None},
    InputAction.SetTrainStopped                                 : {"index": 216, "length":     1, "decoder": None},
    InputAction.ChangeControllerSpeed                           : {"index": 217, "length":     8, "decoder": None},
    InputAction.SetAllowCommands                                : {"index": 218, "length":     1, "decoder": None},
    InputAction.SetResearchFinishedStopsGame                    : {"index": 219, "length":     1, "decoder": None},
    InputAction.SetInserterMaxStackSize                         : {"index": 220, "length":     1, "decoder": None},
    InputAction.OpenTrainGui                                    : {"index": 221, "length":     4, "decoder": None},
    InputAction.SetEntityColor                                  : {"index": 222, "length":     4, "decoder": None},
    InputAction.SetDeconstructionItemTreesAndRocksOnly          : {"index": 223, "length":     1, "decoder": None},
    InputAction.SetDeconstructionItemTileSelectionMode          : {"index": 224, "length":     1, "decoder": None},
    InputAction.DeleteCustomTag                                 : {"index": 225, "length":     4, "decoder": None},
    InputAction.DeletePermissionGroup                           : {"index": 226, "length":     4, "decoder": None},
    InputAction.AddPermissionGroup                              : {"index": 227, "length":     4, "decoder": None},
    InputAction.SetInfinityContainerRemoveUnfilteredItems       : {"index": 228, "length":     1, "decoder": None},
    InputAction.SetCarWeaponsControl                            : {"index": 229, "length":     1, "decoder": None},
    InputAction.SetRequestFromBuffers                           : {"index": 230, "length":     1, "decoder": None},
    InputAction.ChangeActiveQuickBar                            : {"index": 231, "length":     1, "decoder": None},
    InputAction.OpenPermissionsGui                              : {"index": 232, "length":     1, "decoder": None},
    InputAction.DisplayScaleChanged                             : {"index": 233, "length":     8, "decoder": None},
    InputAction.SetSplitterPriority                             : {"index": 234, "length":     1, "decoder": None},
    InputAction.GrabInternalBlueprintFromText                   : {"index": 235, "length":     4, "decoder": None},
    InputAction.SetHeatInterfaceTemperature                     : {"index": 236, "length":     8, "decoder": None},
    InputAction.SetHeatInterfaceMode                            : {"index": 237, "length":     1, "decoder": None},
    InputAction.OpenTrainStationGui                             : {"index": 238, "length":     4, "decoder": None},
    InputAction.RemoveTrainStation                              : {"index": 239, "length":     4, "decoder": None},
    InputAction.GoToTrainStation                                : {"index": 240, "length":     4, "decoder": None},
    InputAction.RenderModeChanged                               : {"index": 241, "length":     1, "decoder": None},
    InputAction.PlayerInputMethodChanged                        : {"index": 242, "length":  None, "decoder": None},
    InputAction.SetPlayerColor                                  : {"index": 243, "length":     4, "decoder": None},
    InputAction.PlayerClickedGpsTag                             : {"index": 244, "length":  None, "decoder": None},
    InputAction.SetTrainsLimit                                  : {"index": 245, "length":     4, "decoder": None},
    InputAction.ClearRecipeNotification                         : {"index": 246, "length":  None, "decoder": None},
    InputAction.SetLinkedContainerLinkID                        : {"index": 247, "length":     4, "decoder": None},
    InputAction.GuiHover                                        : {"index": 248, "length":  None, "decoder": None},
    InputAction.GuiLeave                                        : {"index": 249, "length":  None, "decoder": None},
}


def print_updated_lookup_table():
    print("{")
    for index, input_action_type in enumerate(InputAction):
        try:
            lookup_table_entry = INPUT_ACTION_LOOKUP_TABLE[input_action_type]
        except KeyError:
            print(f'    {input_action_type:60}: {{"index": {index:3}, "length":  None, "decoder": None}},')
            continue
        if lookup_table_entry["length"] is None:
            lookup_table_entry["length"] = "None" 
        if lookup_table_entry["decoder"] is None:
            lookup_table_entry["decoder"] = "None"
        print(f'    {input_action_type:60}: {{"index": {index:3}, "length":  {lookup_table_entry["length"]:4}, "decoder": {lookup_table_entry["decoder"]}}},')
    print("}")

if __name__ == "__main__":
    print_updated_lookup_table()