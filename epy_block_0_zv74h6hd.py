import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Sine Wave Generator Block - Outputs 31 Values"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Sine Wave Generator',   # will show up in GRC
            in_sig=None,
            out_sig=[(np.float32, 31)]
        )
        self.angles = np.linspace(0, np.pi, 31)
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        angles = np.linspace(0, np.pi, 31)
        output_items[0][:] = np.cos(self.angles)
        return len(output_items[0])
