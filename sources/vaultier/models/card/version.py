from modelext.version.condition import RequiredFieldEventCondition
from vaultier.models.card.model import Card
from modelext.changes.changes import SOFT_DELETE, INSERT, UPDATE
from modelext.version.manipulator import register_manipulator_signal, ModelCreatedManipulator, ModelUpdatedManipulator, ModelSoftDeletedManipulator, register_manipulator_class, ModelMovedManipulator


def register_signals():
    register_manipulator_class('card_created_manipulator', ModelCreatedManipulator)
    register_manipulator_class('card_updated_manipulator', ModelUpdatedManipulator)
    register_manipulator_class('card_deleted_manipulator', ModelSoftDeletedManipulator)
    register_manipulator_class('card_moved_manipulator', ModelMovedManipulator)

    from vaultier.models.version.model import Version

    register_manipulator_signal(
        version_cls=Version,
        manipulator_id='card_deleted_manipulator',
        condition=RequiredFieldEventCondition(
            required_sender=Card,
            required_fields=['deleted_at'],
            required_event=SOFT_DELETE,
        )
    )

    register_manipulator_signal(
        version_cls=Version,
        manipulator_id='card_updated_manipulator',
        condition=RequiredFieldEventCondition(
            required_sender=Card,
            required_fields=['name', 'description'],
            required_event=UPDATE,
        )
    )

    register_manipulator_signal(
        version_cls=Version,
        manipulator_id='card_created_manipulator',
        condition=RequiredFieldEventCondition(
            required_sender=Card,
            required_fields=None,
            required_event=INSERT,
        )
    )

    register_manipulator_signal(
        version_cls=Version,
        manipulator_id='card_moved_manipulator',
        condition=RequiredFieldEventCondition(
            required_sender=Card,
            required_fields=['vault_id'],
            required_event=UPDATE,
        )
    )



