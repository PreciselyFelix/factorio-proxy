from enum import Enum

class SynchronizerActionType(Enum):
    GameEnd = 0
    PeerDisconnect = 1
    NewPeerInfo = 2
    ClientChangedState = 3
    ClientShouldStartSendingTickClosures = 4
    MapReadyForDownload = 5
    MapLoadingProgressUpdate = 6
    MapSavingProgressUpdate = 7
    SavingForUpdate = 8
    MapDownloadingProgressUpdate = 9
    CatchingUpProgressUpdate = 10
    PeerDroppingProgressUpdate = 11
    PlayerDesynced = 12
    BeginPause = 13
    EndPause = 14
    SkippedTickClosure = 15
    SkippedTickClosureConfirm = 16
    ChangeLatency = 17
    IncreasedLatencyConfirm = 18
    SavingCountDown = 19