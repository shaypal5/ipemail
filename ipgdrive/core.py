"""Core functionalities for ipemail."""

import os

from crontab import CronTab

from .cfg import (
    IPG_CFG,
    CfgKey,
)
from .util import printlog


DPATH = os.path.dirname(os.path.abspath(__file__))
JOB_FPATH = os.path.join(DPATH, 'job.py')
JOB_COMMENT_ID = 'ipgdrive'


def setup_job():
    my_cron = CronTab(user=IPG_CFG[CfgKey.USERNAME])
    minutes = IPG_CFG[CfgKey.FREQ_MINUTES]
    ipg_job = None
    for job in my_cron:
        if job.comment == JOB_COMMENT_ID:
            ipg_job = job
    if ipg_job is None:
        ipg_job = my_cron.new(
            command='ipgdrive run-job',
            comment='ipgdrive',
        )
        ipg_job.minute.every(minutes)
        my_cron.write()
        printlog("New crontab job created for ipgdrive.")
    else:
        printlog("Exsiting crontab job found for ipgdrive.")
        ipg_job.set_command('ipgdrive run-job')
        ipg_job.minute.every(minutes)
        ipg_job.enable()
        my_cron.write()
        printlog(
            "crontab job for ipgdrive updated w minutes={}.".format(minutes))


if __name__ == "__main__":
    setup_job()
