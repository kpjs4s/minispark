
class Config(object):
    MIN_TIME_TO_PREEMPT_TASK = 0
    HEART_BEAT_TIME_INTREVAL = 3
    WORKER_SLEEP_FOR_HEART_BEAT = 1
    MASTER_IP = "tcp://0.0.0.0:9000"

    OUTPUT_DIR = "/home/kannan/school/cs636/Default-project2/output/"

    WORKER_STATUS_REDUCE_FAILED = -1
    WORKER_STATUS_IDLE = 0
    WORKER_STATUS_COMPLETE = 1
    WORKER_STATUS_WORKING_JOB = 2
    WORKER_STATUS_WORKING_REDUCE = 3
    WORKER_STATUS_WORKING_SHUFFLE = 4
    # WORKER_STATUS_COMPLETE_REDUCE = 5