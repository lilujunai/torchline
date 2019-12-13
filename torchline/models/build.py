from torchline.utils import Registry

META_ARCH_REGISTRY = Registry("META_ARCH")
META_ARCH_REGISTRY.__doc__ = """
Registry for meta-architectures, i.e. the whole model.

The registered object will be called with `obj(cfg)`
and expected to return a `nn.Module` object.
"""


def build_model(cfg):
    """
    Built the whole model, defined by `cfg.MODEL.META_ARCH`.
    """
    meta_arch = cfg.MODEL.META_ARCH
    return META_ARCH_REGISTRY.get(meta_arch)(cfg)
    