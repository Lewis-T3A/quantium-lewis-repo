from app import app


def find_by_id(component, target_id):
    if getattr(component, "id", None) == target_id:
        return component

    children = getattr(component, "children", None)

    if children is None:
        return None

    if isinstance(children, (list, tuple)):
        for child in children:
            result = find_by_id(child, target_id)
            if result is not None:
                return result
    else:
        result = find_by_id(children, target_id)
        if result is not None:
            return result

    return None


def test_header_present():
    header = find_by_id(app.layout, "app-header")
    assert header is not None
    assert header.children == "Pink Morsel Sales Visualiser"


def test_region_picker_present():
    radio = find_by_id(app.layout, "region-filter")
    assert radio is not None


def test_visualisation_present():
    graph = find_by_id(app.layout, "sales-chart")
    assert graph is not None