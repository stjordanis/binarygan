"""Network architecture for the discriminator for the real-valued model
implemented by MLPs."""
NET_D = {}

NET_D['main'] = [
    ('reshape', 784),              # 0
    ('dense', 512, None, 'lrelu'), # 1
    ('dense', 256, None, 'lrelu'), # 2
    ('dense', 1),                  # 3
]
