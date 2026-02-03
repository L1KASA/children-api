from children.models import Child


class ChildService:
    @staticmethod
    def get_all_children() -> list[dict[str, int | str]]:
        """
        Получить всех детей
        """
        children = Child.objects.all()

        result = []

        for child in children:
            result.append({
                'id': child.id,
                'full_name': child.full_name,
                'cyberons': child.cyberons,
                'status': child.status,
                'status_display': child.get_status_display(),
                'created_at': child.created_at.isoformat(),
                'updated_at': child.updated_at.isoformat(),
            })

        return result

    @staticmethod
    def get_children_count() -> int:
        """Получить количество детей"""
        return Child.objects.count()
