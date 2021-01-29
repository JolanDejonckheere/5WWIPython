def dubbels(lijst):
    resultaat = []

    for element in lijst:
        # als element 2 x voorkomt in lijst EN element nog niet voorkomt in resultaat
        if lijst.count(element) > 1 and element not in resultaat:
            resultaat.append(element)

    return resultaat
