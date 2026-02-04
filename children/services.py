from children.models import Child


class ChildService:
    @staticmethod
    def validate_status(status: str) -> bool:
        """Валидация статуса"""
        if not status:
            return True

        valid_statuses = [choice[0] for choice in Child.Status.choices]
        return status in valid_statuses

    @staticmethod
    def get_all_children(status_filter: str = None) -> list[dict[str, int | str]]:
        """
        Получить всех детей с возможностью фильтрации по полям

        Args:
            status_filter: Фильтр по статусу. По умолчанию None.
        """
        if status_filter and not ChildService.validate_status(status_filter):
            raise ValueError(f"Некорректный статус: {status_filter}")

        children = Child.objects.all()

        if status_filter:
            children = children.filter(status=status_filter)

        result = []

        for child in children:
            result.append({
                'id': child.id,
                'full_name': child.full_name,
                'cyberons': child.cyberons,
                'status': child.status,
                'created_at': child.created_at.isoformat(),
                'updated_at': child.updated_at.isoformat(),
            })

        return result

    @staticmethod
    def get_children_count(status_filter: str = None) -> int:
        """Получить количество детей с возможностью фильтрации по полям"""
        queryset = Child.objects.all()
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        return queryset.count()
