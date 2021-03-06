"""Factory default HPCOM7 devices.
"""


class CleanErase(object):
    """Factory default a HP Comware 7 switch.

    Args:
        device (HPCOM7): connected instance of a ``pyhpecw7.comware.HPCOM7``
            object.

    Attributes:
        device (HPCOM7): connected instance of a ``pyhpecw7.comware.HPCOM7``
            object.
    """

    def __init__(self, device):
        self.device = device

    def build(self, stage=False, factory_default=False):
        """Build cmd list to factory default switch and immediately reboot.

        Args:
            factory_default (bool): determines if the switch will be
                reset to factory defaults.  It is a safety measure and
                must be set to for the factory default to take place.
            stage (bool): whether to stage the command for later execution,
                or execute immediately.
        Returns:
            True if stage=True and staging is successful.
            The output of restore command if stage=False
        """
        if factory_default:
            commands = ['restore factory-default']
            if stage:
                return self.device.stage_config(commands, 'cli_display')
            else:
                try:
                    return self.device.cli_display(commands)
                finally:
                    self.device.reboot()
