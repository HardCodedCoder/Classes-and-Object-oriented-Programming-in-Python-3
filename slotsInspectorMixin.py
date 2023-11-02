class SlotsInspectorMixin:

    # If we do not define slots here, the developer class would have an empty dictionary as it inherits from this class.
    __slots__ = ()

    def has_slots(self) -> bool:
        return hasattr(self, "__slots__")