from enum import Enum

class InputActionType(Enum):
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


INPUT_ACTION_LOOKUP_TABLE = {
    InputActionType.Nothing                                         : {"index":   0, "length":     0, "decoder": None},
    InputActionType.StopWalking                                     : {"index":   1, "length":     0, "decoder": None},
    InputActionType.BeginMining                                     : {"index":   2, "length":     0, "decoder": None},
    InputActionType.StopMining                                      : {"index":   3, "length":     0, "decoder": None},
    InputActionType.ToggleDriving                                   : {"index":   4, "length":     0, "decoder": None},
    InputActionType.OpenGui                                         : {"index":   5, "length":     0, "decoder": None},
    InputActionType.CloseGui                                        : {"index":   6, "length":     0, "decoder": None},
    InputActionType.OpenCharacterGui                                : {"index":   7, "length":     0, "decoder": None},
    InputActionType.OpenCurrentVehicleGui                           : {"index":   8, "length":     0, "decoder": None},
    InputActionType.ConnectRollingStock                             : {"index":   9, "length":     0, "decoder": None},
    InputActionType.DisconnectRollingStock                          : {"index":  10, "length":     0, "decoder": None},
    InputActionType.SelectedEntityCleared                           : {"index":  11, "length":     0, "decoder": None},
    InputActionType.ClearCursor                                     : {"index":  12, "length":     0, "decoder": None},
    InputActionType.ResetAssemblingMachine                          : {"index":  13, "length":     0, "decoder": None},
    InputActionType.OpenTechnologyGui                               : {"index":  14, "length":     0, "decoder": None},
    InputActionType.LaunchRocket                                    : {"index":  15, "length":     0, "decoder": None},
    InputActionType.OpenProductionGui                               : {"index":  16, "length":     0, "decoder": None},
    InputActionType.StopRepair                                      : {"index":  17, "length":     0, "decoder": None},
    InputActionType.CancelNewBlueprint                              : {"index":  18, "length":     0, "decoder": None},
    InputActionType.CloseBlueprintRecord                            : {"index":  19, "length":     0, "decoder": None},
    InputActionType.CopyEntitySettings                              : {"index":  20, "length":     0, "decoder": None},
    InputActionType.PasteEntitySettings                             : {"index":  21, "length":     0, "decoder": None},
    InputActionType.DestroyOpenedItem                               : {"index":  22, "length":     0, "decoder": None},
    InputActionType.CopyOpenedItem                                  : {"index":  23, "length":     0, "decoder": None},
    InputActionType.ToggleShowEntityInfo                            : {"index":  24, "length":     0, "decoder": None},
    InputActionType.SingleplayerInit                                : {"index":  25, "length":     0, "decoder": None},
    InputActionType.MultiplayerInit                                 : {"index":  26, "length":     0, "decoder": None},
    InputActionType.DisconnectAllPlayers                            : {"index":  27, "length":     0, "decoder": None},
    InputActionType.SwitchToRenameStopGui                           : {"index":  28, "length":     0, "decoder": None},
    InputActionType.OpenBonusGui                                    : {"index":  29, "length":     0, "decoder": None},
    InputActionType.OpenTrainsGui                                   : {"index":  30, "length":     0, "decoder": None},
    InputActionType.OpenAchievementsGui                             : {"index":  31, "length":     0, "decoder": None},
    InputActionType.CycleBlueprintBookForwards                      : {"index":  32, "length":     0, "decoder": None},
    InputActionType.CycleBlueprintBookBackwards                     : {"index":  33, "length":     0, "decoder": None},
    InputActionType.CycleClipboardForwards                          : {"index":  34, "length":     0, "decoder": None},
    InputActionType.CycleClipboardBackwards                         : {"index":  35, "length":     0, "decoder": None},
    InputActionType.StopMovementInTheNextTick                       : {"index":  36, "length":     0, "decoder": None},
    InputActionType.ToggleEnableVehicleLogisticsWhileMoving         : {"index":  37, "length":     0, "decoder": None},
    InputActionType.ToggleDeconstructionItemEntityFilterMode        : {"index":  38, "length":     0, "decoder": None},
    InputActionType.ToggleDeconstructionItemTileFilterMode          : {"index":  39, "length":     0, "decoder": None},
    InputActionType.OpenLogisticGui                                 : {"index":  40, "length":     0, "decoder": None},
    InputActionType.SelectNextValidGun                              : {"index":  41, "length":     0, "decoder": None},
    InputActionType.ToggleMapEditor                                 : {"index":  42, "length":     0, "decoder": None},
    InputActionType.DeleteBlueprintLibrary                          : {"index":  43, "length":     0, "decoder": None},
    InputActionType.GameCreatedFromScenario                         : {"index":  44, "length":     0, "decoder": None},
    InputActionType.ActivateCopy                                    : {"index":  45, "length":     0, "decoder": None},
    InputActionType.ActivateCut                                     : {"index":  46, "length":     0, "decoder": None},
    InputActionType.ActivatePaste                                   : {"index":  47, "length":     0, "decoder": None},
    InputActionType.Undo                                            : {"index":  48, "length":     0, "decoder": None},
    InputActionType.TogglePersonalRoboport                          : {"index":  49, "length":     0, "decoder": None},
    InputActionType.ToggleEquipmentMovementBonus                    : {"index":  50, "length":     0, "decoder": None},
    InputActionType.TogglePersonalLogisticRequests                  : {"index":  51, "length":     0, "decoder": None},
    InputActionType.ToggleEntityLogisticRequests                    : {"index":  52, "length":     0, "decoder": None},
    InputActionType.StopBuildingByMoving                            : {"index":  53, "length":     0, "decoder": None},
    InputActionType.FlushOpenedEntityFluid                          : {"index":  54, "length":     0, "decoder": None},
    InputActionType.ForceFullCRC                                    : {"index":  55, "length":     0, "decoder": None},
    InputActionType.OpenTipsAndTricksGui                            : {"index":  56, "length":     4, "decoder": None},
    InputActionType.OpenBlueprintLibraryGui                         : {"index":  57, "length":     2, "decoder": None},
    InputActionType.ChangeBlueprintLibraryTab                       : {"index":  58, "length":     3, "decoder": None},
    InputActionType.DropItem                                        : {"index":  59, "length":     8, "decoder": None},
    InputActionType.Build                                           : {"index":  60, "length":     5, "decoder": None},
    InputActionType.StartWalking                                    : {"index":  61, "length":     1, "decoder": None},
    InputActionType.BeginMiningTerrain                              : {"index":  62, "length":     8, "decoder": None},
    InputActionType.ChangeRidingState                               : {"index":  63, "length":     2, "decoder": None},
    InputActionType.OpenItem                                        : {"index":  64, "length":     5, "decoder": None},
    InputActionType.OpenParentOfOpenedItem                          : {"index":  65, "length":     2, "decoder": None},
    InputActionType.ResetItem                                       : {"index":  66, "length":     5, "decoder": None},
    InputActionType.DestroyItem                                     : {"index":  67, "length":     8, "decoder": None},
    InputActionType.OpenModItem                                     : {"index":  68, "length":     6, "decoder": None},
    InputActionType.OpenEquipment                                   : {"index":  69, "length":  None, "decoder": None},
    InputActionType.CursorTransfer                                  : {"index":  70, "length":     9, "decoder": None},
    InputActionType.CursorSplit                                     : {"index":  71, "length":     5, "decoder": None},
    InputActionType.StackTransfer                                   : {"index":  72, "length":     5, "decoder": None},
    InputActionType.InventoryTransfer                               : {"index":  73, "length":     5, "decoder": None},
    InputActionType.CheckCRCHeuristic                               : {"index":  74, "length":    11, "decoder": None},
    InputActionType.Craft                                           : {"index":  75, "length":     5, "decoder": None},
    InputActionType.WireDragging                                    : {"index":  76, "length":     8, "decoder": None},
    InputActionType.ChangeShootingState                             : {"index":  77, "length":     9, "decoder": None},
    InputActionType.SetupAssemblingMachine                          : {"index":  78, "length":  None, "decoder": None},
    InputActionType.SelectedEntityChanged                           : {"index":  79, "length":     8, "decoder": None},
    InputActionType.SmartPipette                                    : {"index":  80, "length":  None, "decoder": None},
    InputActionType.StackSplit                                      : {"index":  81, "length":     2, "decoder": None},
    InputActionType.InventorySplit                                  : {"index":  82, "length":     8, "decoder": None},
    InputActionType.CancelCraft                                     : {"index":  83, "length":  None, "decoder": None},
    InputActionType.SetFilter                                       : {"index":  84, "length":  None, "decoder": None},
    InputActionType.CheckCRC                                        : {"index":  85, "length":     9, "decoder": None},
    InputActionType.SetCircuitCondition                             : {"index":  86, "length":  None, "decoder": None},
    InputActionType.SetSignal                                       : {"index":  87, "length":  None, "decoder": None},
    InputActionType.StartResearch                                   : {"index":  88, "length":  None, "decoder": None},
    InputActionType.SetLogisticFilterItem                           : {"index":  89, "length":  None, "decoder": None},
    InputActionType.SetLogisticFilterSignal                         : {"index":  90, "length":     1, "decoder": None},
    InputActionType.SetCircuitModeOfOperation                       : {"index":  91, "length":    12, "decoder": None},
    InputActionType.GuiClick                                        : {"index":  92, "length":  None, "decoder": None},
    InputActionType.GuiConfirmed                                    : {"index":  93, "length":  None, "decoder": None},
    InputActionType.WriteToConsole                                  : {"index":  94, "length":  None, "decoder": None},
    InputActionType.MarketOffer                                     : {"index":  95, "length":     9, "decoder": None},
    InputActionType.AddTrainStation                                 : {"index":  96, "length":     9, "decoder": None},
    InputActionType.ChangeTrainStopStation                          : {"index":  97, "length":  None, "decoder": None},
    InputActionType.ChangeActiveItemGroupForCrafting                : {"index":  98, "length":    25, "decoder": None},
    InputActionType.ChangeActiveItemGroupForFilters                 : {"index":  99, "length":     5, "decoder": None},
    InputActionType.ChangeActiveCharacterTab                        : {"index": 100, "length":     1, "decoder": None},
    InputActionType.GuiTextChanged                                  : {"index": 101, "length":  None, "decoder": None},
    InputActionType.GuiCheckedStateChanged                          : {"index": 102, "length":     8, "decoder": None},
    InputActionType.GuiSelectionStateChanged                        : {"index": 103, "length":  None, "decoder": None},
    InputActionType.GuiSelectedTabChanged                           : {"index": 104, "length":  None, "decoder": None},
    InputActionType.GuiValueChanged                                 : {"index": 105, "length":    23, "decoder": None},
    InputActionType.GuiSwitchStateChanged                           : {"index": 106, "length":  None, "decoder": None},
    InputActionType.GuiLocationChanged                              : {"index": 107, "length":    23, "decoder": None},
    InputActionType.PlaceEquipment                                  : {"index": 108, "length":  None, "decoder": None},
    InputActionType.TakeEquipment                                   : {"index": 109, "length":  None, "decoder": None},
    InputActionType.UseItem                                         : {"index": 110, "length":     8, "decoder": None},
    InputActionType.SendSpidertron                                  : {"index": 111, "length":  None, "decoder": None},
    InputActionType.UseArtilleryRemote                              : {"index": 112, "length":     8, "decoder": None},
    InputActionType.SetInventoryBar                                 : {"index": 113, "length":     6, "decoder": None},
    InputActionType.MoveOnZoom                                      : {"index": 114, "length":  None, "decoder": None},
    InputActionType.StartRepair                                     : {"index": 115, "length":     8, "decoder": None},
    InputActionType.Deconstruct                                     : {"index": 116, "length":     8, "decoder": None},
    InputActionType.Upgrade                                         : {"index": 117, "length":  None, "decoder": None},
    InputActionType.Copy                                            : {"index": 118, "length":     2, "decoder": None},
    InputActionType.AlternativeCopy                                 : {"index": 119, "length":  None, "decoder": None},
    InputActionType.SelectBlueprintEntities                         : {"index": 120, "length":  None, "decoder": None},
    InputActionType.AltSelectBlueprintEntities                      : {"index": 121, "length":  None, "decoder": None},
    InputActionType.SetupBlueprint                                  : {"index": 122, "length":  None, "decoder": None},
    InputActionType.SetupSingleBlueprintRecord                      : {"index": 123, "length":  None, "decoder": None},
    InputActionType.CopyOpenedBlueprint                             : {"index": 124, "length":  None, "decoder": None},
    InputActionType.ReassignBlueprint                               : {"index": 125, "length":  None, "decoder": None},
    InputActionType.OpenBlueprintRecord                             : {"index": 126, "length":  None, "decoder": None},
    InputActionType.GrabBlueprintRecord                             : {"index": 127, "length":  None, "decoder": None},
    InputActionType.DropBlueprintRecord                             : {"index": 128, "length":  None, "decoder": None},
    InputActionType.DeleteBlueprintRecord                           : {"index": 129, "length":  None, "decoder": None},
    InputActionType.UpgradeOpenedBlueprintByRecord                  : {"index": 130, "length":  None, "decoder": None},
    InputActionType.UpgradeOpenedBlueprintByItem                    : {"index": 131, "length":  None, "decoder": None},
    InputActionType.SpawnItem                                       : {"index": 132, "length":  None, "decoder": None},
    InputActionType.SpawnItemStackTransfer                          : {"index": 133, "length":  None, "decoder": None},
    InputActionType.UpdateBlueprintShelf                            : {"index": 134, "length":  None, "decoder": None},
    InputActionType.TransferBlueprint                               : {"index": 135, "length":    13, "decoder": None},
    InputActionType.TransferBlueprintImmediately                    : {"index": 136, "length":    10, "decoder": None},
    InputActionType.EditBlueprintToolPreview                        : {"index": 137, "length":  None, "decoder": None},
    InputActionType.RemoveCables                                    : {"index": 138, "length":     8, "decoder": None},
    InputActionType.ExportBlueprint                                 : {"index": 139, "length":  None, "decoder": None},
    InputActionType.ImportBlueprint                                 : {"index": 140, "length":    16, "decoder": None},
    InputActionType.ImportBlueprintsFiltered                        : {"index": 141, "length":     6, "decoder": None},
    InputActionType.PlayerJoinGame                                  : {"index": 142, "length":  None, "decoder": None},
    InputActionType.PlayerAdminChange                               : {"index": 143, "length":     1, "decoder": None},
    InputActionType.CancelDeconstruct                               : {"index": 144, "length":  None, "decoder": None},
    InputActionType.CancelUpgrade                                   : {"index": 145, "length":     5, "decoder": None},
    InputActionType.ChangeArithmeticCombinatorParameters            : {"index": 146, "length":  None, "decoder": None},
    InputActionType.ChangeDeciderCombinatorParameters               : {"index": 147, "length":  None, "decoder": None},
    InputActionType.ChangeProgrammableSpeakerParameters             : {"index": 148, "length":  None, "decoder": None},
    InputActionType.ChangeProgrammableSpeakerAlertParameters        : {"index": 149, "length":  None, "decoder": None},
    InputActionType.ChangeProgrammableSpeakerCircuitParameters      : {"index": 150, "length":  None, "decoder": None},
    InputActionType.SetVehicleAutomaticTargetingParameters          : {"index": 151, "length":  None, "decoder": None},
    InputActionType.BuildTerrain                                    : {"index": 152, "length":  None, "decoder": None},
    InputActionType.ChangeTrainWaitCondition                        : {"index": 153, "length":  None, "decoder": None},
    InputActionType.ChangeTrainWaitConditionData                    : {"index": 154, "length":  None, "decoder": None},
    InputActionType.CustomInput                                     : {"index": 155, "length":  None, "decoder": None},
    InputActionType.ChangeItemLabel                                 : {"index": 156, "length":  None, "decoder": None},
    InputActionType.ChangeItemDescription                           : {"index": 157, "length":  None, "decoder": None},
    InputActionType.ChangeEntityLabel                               : {"index": 158, "length":  None, "decoder": None},
    InputActionType.BuildRail                                       : {"index": 159, "length":  None, "decoder": None},
    InputActionType.CancelResearch                                  : {"index": 160, "length":    12, "decoder": None},
    InputActionType.SelectArea                                      : {"index": 161, "length":  None, "decoder": None},
    InputActionType.AltSelectArea                                   : {"index": 162, "length":  None, "decoder": None},
    InputActionType.ReverseSelectArea                               : {"index": 163, "length":  None, "decoder": None},
    InputActionType.AltReverseSelectArea                            : {"index": 164, "length":  None, "decoder": None},
    InputActionType.ServerCommand                                   : {"index": 165, "length":     4, "decoder": None},
    InputActionType.SetControllerLogisticTrashFilterItem            : {"index": 166, "length":  None, "decoder": None},
    InputActionType.SetEntityLogisticTrashFilterItem                : {"index": 167, "length":  None, "decoder": None},
    InputActionType.SetInfinityContainerFilterItem                  : {"index": 168, "length":  None, "decoder": None},
    InputActionType.SetInfinityPipeFilter                           : {"index": 169, "length":     8, "decoder": None},
    InputActionType.ModSettingsChanged                              : {"index": 170, "length":     7, "decoder": None},
    InputActionType.SetEntityEnergyProperty                         : {"index": 171, "length":     4, "decoder": None},
    InputActionType.EditCustomTag                                   : {"index": 172, "length":     2, "decoder": None},
    InputActionType.EditPermissionGroup                             : {"index": 173, "length":     1, "decoder": None},
    InputActionType.ImportBlueprintString                           : {"index": 174, "length":  None, "decoder": None},
    InputActionType.ImportPermissionsString                         : {"index": 175, "length":  None, "decoder": None},
    InputActionType.ReloadScript                                    : {"index": 176, "length":  None, "decoder": None},
    InputActionType.ReloadScriptDataTooLarge                        : {"index": 177, "length":  None, "decoder": None},
    InputActionType.GuiElemChanged                                  : {"index": 178, "length":  None, "decoder": None},
    InputActionType.BlueprintTransferQueueUpdate                    : {"index": 179, "length":     1, "decoder": None},
    InputActionType.DragTrainSchedule                               : {"index": 180, "length":     1, "decoder": None},
    InputActionType.DragTrainWaitCondition                          : {"index": 181, "length":     2, "decoder": None},
    InputActionType.SelectItem                                      : {"index": 182, "length":     4, "decoder": None},
    InputActionType.SelectEntitySlot                                : {"index": 183, "length":     4, "decoder": None},
    InputActionType.SelectTileSlot                                  : {"index": 184, "length":  None, "decoder": None},
    InputActionType.SelectMapperSlot                                : {"index": 185, "length":  None, "decoder": None},
    InputActionType.DisplayResolutionChanged                        : {"index": 186, "length":  None, "decoder": None},
    InputActionType.QuickBarSetSlot                                 : {"index": 187, "length":  None, "decoder": None},
    InputActionType.QuickBarPickSlot                                : {"index": 188, "length":  None, "decoder": None}, # data_type: ByteColor?
    InputActionType.QuickBarSetSelectedPage                         : {"index": 189, "length":  None, "decoder": None}, # data_type unknown complex
    InputActionType.PlayerLeaveGame                                 : {"index": 190, "length":     1, "decoder": None},
    InputActionType.MapEditorAction                                 : {"index": 191, "length":     1, "decoder": None},
    InputActionType.PutSpecialItemInMap                             : {"index": 192, "length":     1, "decoder": None},
    InputActionType.PutSpecialRecordInMap                           : {"index": 193, "length":     1, "decoder": None},
    InputActionType.ChangeMultiplayerConfig                         : {"index": 194, "length":     1, "decoder": None},
    InputActionType.AdminAction                                     : {"index": 195, "length":  None, "decoder": None}, # data_type: adminActionData
    InputActionType.LuaShortcut                                     : {"index": 196, "length":  None, "decoder": None}, # data_type unknown complex
    InputActionType.TranslateString                                 : {"index": 197, "length":  None, "decoder": None}, # data_type unknown complex
    InputActionType.FlushOpenedEntitySpecificFluid                  : {"index": 198, "length":  None, "decoder": None}, # data_type unknown complex
    InputActionType.ChangePickingState                              : {"index": 199, "length":     1, "decoder": None},
    InputActionType.SelectedEntityChangedVeryClose                  : {"index": 200, "length":     1, "decoder": None},
    InputActionType.SelectedEntityChangedVeryClosePrecise           : {"index": 201, "length":     2, "decoder": None},
    InputActionType.SelectedEntityChangedRelative                   : {"index": 202, "length":     4, "decoder": None},
    InputActionType.SelectedEntityChangedBasedOnUnitNumber          : {"index": 203, "length":     4, "decoder": None},
    InputActionType.SetAutosortInventory                            : {"index": 204, "length":     1, "decoder": None},
    InputActionType.SetFlatControllerGui                            : {"index": 205, "length":     1, "decoder": None},
    InputActionType.SetRecipeNotifications                          : {"index": 206, "length":     1, "decoder": None},
    InputActionType.SetAutoLaunchRocket                             : {"index": 207, "length":     2, "decoder": None},
    InputActionType.SwitchConstantCombinatorState                   : {"index": 208, "length":     1, "decoder": None},
    InputActionType.SwitchPowerSwitchState                          : {"index": 209, "length":     1, "decoder": None},
    InputActionType.SwitchInserterFilterModeState                   : {"index": 210, "length":     1, "decoder": None},
    InputActionType.SwitchConnectToLogisticNetwork                  : {"index": 211, "length":     1, "decoder": None},
    InputActionType.SetBehaviorMode                                 : {"index": 212, "length":     1, "decoder": None},
    InputActionType.FastEntityTransfer                              : {"index": 213, "length":     1, "decoder": None},
    InputActionType.RotateEntity                                    : {"index": 214, "length":     1, "decoder": None},
    InputActionType.FastEntitySplit                                 : {"index": 215, "length":     1, "decoder": None},
    InputActionType.SetTrainStopped                                 : {"index": 216, "length":     1, "decoder": None},
    InputActionType.ChangeControllerSpeed                           : {"index": 217, "length":     8, "decoder": None},
    InputActionType.SetAllowCommands                                : {"index": 218, "length":     1, "decoder": None},
    InputActionType.SetResearchFinishedStopsGame                    : {"index": 219, "length":     1, "decoder": None},
    InputActionType.SetInserterMaxStackSize                         : {"index": 220, "length":     1, "decoder": None},
    InputActionType.OpenTrainGui                                    : {"index": 221, "length":     4, "decoder": None},
    InputActionType.SetEntityColor                                  : {"index": 222, "length":     4, "decoder": None},
    InputActionType.SetDeconstructionItemTreesAndRocksOnly          : {"index": 223, "length":     1, "decoder": None},
    InputActionType.SetDeconstructionItemTileSelectionMode          : {"index": 224, "length":     1, "decoder": None},
    InputActionType.DeleteCustomTag                                 : {"index": 225, "length":     4, "decoder": None},
    InputActionType.DeletePermissionGroup                           : {"index": 226, "length":     4, "decoder": None},
    InputActionType.AddPermissionGroup                              : {"index": 227, "length":     4, "decoder": None},
    InputActionType.SetInfinityContainerRemoveUnfilteredItems       : {"index": 228, "length":     1, "decoder": None},
    InputActionType.SetCarWeaponsControl                            : {"index": 229, "length":     1, "decoder": None},
    InputActionType.SetRequestFromBuffers                           : {"index": 230, "length":     1, "decoder": None},
    InputActionType.ChangeActiveQuickBar                            : {"index": 231, "length":     1, "decoder": None},
    InputActionType.OpenPermissionsGui                              : {"index": 232, "length":     1, "decoder": None},
    InputActionType.DisplayScaleChanged                             : {"index": 233, "length":     8, "decoder": None},
    InputActionType.SetSplitterPriority                             : {"index": 234, "length":     1, "decoder": None},
    InputActionType.GrabInternalBlueprintFromText                   : {"index": 235, "length":     4, "decoder": None},
    InputActionType.SetHeatInterfaceTemperature                     : {"index": 236, "length":     8, "decoder": None},
    InputActionType.SetHeatInterfaceMode                            : {"index": 237, "length":     1, "decoder": None},
    InputActionType.OpenTrainStationGui                             : {"index": 238, "length":     4, "decoder": None},
    InputActionType.RemoveTrainStation                              : {"index": 239, "length":     4, "decoder": None},
    InputActionType.GoToTrainStation                                : {"index": 240, "length":     4, "decoder": None},
    InputActionType.RenderModeChanged                               : {"index": 241, "length":     1, "decoder": None},
    InputActionType.PlayerInputMethodChanged                        : {"index": 242, "length":     1, "decoder": None}, 
    InputActionType.SetPlayerColor                                  : {"index": 243, "length":     4, "decoder": None},
    InputActionType.PlayerClickedGpsTag                             : {"index": 244, "length":  None, "decoder": None}, # data_type: pingCoordinates
    InputActionType.SetTrainsLimit                                  : {"index": 245, "length":     4, "decoder": None},
    InputActionType.ClearRecipeNotification                         : {"index": 246, "length":  None, "decoder": None}, # data_type unknown complex
    InputActionType.SetLinkedContainerLinkID                        : {"index": 247, "length":     4, "decoder": None},
    InputActionType.GuiHover                                        : {"index": 248, "length":     4, "decoder": None},
    InputActionType.GuiLeave                                        : {"index": 249, "length":     4, "decoder": None},
}


def print_updated_lookup_table():
    print("{")
    for index, input_action_type in enumerate(InputActionType):
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