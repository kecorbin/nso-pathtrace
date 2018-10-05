import ncs
from ncs.dp import Action
import ncs.maapi as maapi
import ncs.maagic as maagic


def ping(devs, devname, dest):
    """
    execute live status ping from dev to destination
    """
    ping = devs[devname].live_status.__getitem__('exec').ping
    inp = ping.get_input()
    inp.args = [dest]
    res = ping.request(inp)
    return res.result


def traceroute(devs, devname, dest):
    """
    execute live status traceroute from dev to destination
    """
    ping = devs[devname].live_status.__getitem__('exec').traceroute
    inp = ping.get_input()
    inp.args = [dest]
    res = ping.request(inp)
    return res.result


class Run(Action):
    @Action.action
    def cb_action(self, uinfo, _name, kp, input, output):
        # actions have access to the CDB.
        with maapi.single_read_trans(uinfo.username, 'pathtrace') as cfg:
            svc = maagic.get_node(cfg, kp)
            root = ncs.maagic.get_root(cfg)
            devs = root.devices.device
            msg = "running pathtrace from {} to {}"
            self.log.info(msg.format(svc.device, svc.destination))
            p = ping(devs, svc.device, svc.destination)
            t = traceroute(devs, svc.device, svc.destination)

        output.result = p + t
        output.ready = True
