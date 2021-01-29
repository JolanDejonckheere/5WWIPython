deelnemers = ['jan', 'piet', 'joris', 'korneel']
moordenaar = 'joris'

def ik_heb_gemoord(deelnemers, moordenaar):
    slachtoffer = deelnemers[(deelnemers.index(moordenaar) + 1) % len(deelnemers)]
    volgend_slachtoffer = deelnemers[(deelnemers.index(slachtoffer) + 1) % len(deelnemers)]
    overige_deelnemers = deelnemers.remove(slachtoffer)

    return volgend_slachtoffer, overige_deelnemers



