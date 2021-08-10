#full credits friday ot thanks friday bot ⚡
#kang with credits else gay

from pokedex import pokedex

from . import CMD_HELP
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="pokedex (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    pokedx = pokedex.Pokedex()
    pokemen = pokedx.get_pokemon_by_name(input_str)
    pokemon = pokemen[0]
    name = str(pokemon.get("name"))
    number = str(pokemon.get("number"))
    species = str(pokemon.get("species"))
    typo = pokemon.get("types")
    types = "".join(str(tu) + ",  " for tu in typo)
    lol = pokemon.get("abilities")
    lmao = lol.get("normal")
    ok = ""
    for ty in lmao:
        ok = str(ty) + ",  "

    kk = lol.get("hidden")
    hm = "".join(str(pq) + ",  " for pq in kk)
    hell = pokemon.get("eggGroups")
    uio = "".join(str(x) + ",  " for x in hell)
    height = pokemon.get("height")
    weight = pokemon.get("weight")
    yes = pokemon.get("family")
    Id = str(yes.get("id"))
    evo = str(yes.get("evolutionStage"))
    pol = yes.get("evolutionLine")
    xy = "".join(str(p) + ",  " for p in pol)
    start = pokemon.get("starter")
    if start == False:
        start = "No"
    elif start == True:
        start = "True"
    leg = pokemon.get("legendary")

    if leg == False:
        leg = "No"
    elif leg == True:
        leg = "True"
    myt = pokemon.get("mythical")
    if myt == False:
        myt = "No"
    elif myt == True:
        myt = "True"
    ultra = pokemon.get("ultraBeast")

    if ultra == False:
        ultra = "No"
    elif ultra == True:
        ultra = "True"
    megA = pokemon.get("mega")

    if megA == False:
        megA = "No"
    elif megA == True:
        megA = "True"
    gEn = pokemon.get("gen")
    link = pokemon.get("sprite")
    des = pokemon.get("description")

    # hope = await borg(event.chat_id, link)
    caption = f"<b><u>Pokemon Information Gathered Successfully</b></u>\n\n\n<b>Name:-   {name}\nNumber:-  {number}\nSpecies:- {species}\nType:- {types}\n\n<u>Abilities</u>\nNormal Abilities:- {ok}\nHidden Abilities:- {hm}\nEgg Group:-  {uio}\nHeight:- {height}\nWeight:- {weight}\n\n<u>Family</u>\nID:- {Id}\nEvolution Stage:- {evo}\nEvolution Line:- {xy}\nStarter:- {start}\nLegendary:- {leg}\nMythical:- {myt}\nUltra Beast:- {ultra}\nMega:- {megA}\nGen:-  {gEn}\nDescription:-  {des}</b>"

    await borg.send_message(
        event.chat_id,
        caption,
        parse_mode="HTML",
        file=link,
        force_document=False,
        silent=True,
    )
    await event.delete()


CMD_HELP.update(
    {
        "pokedex": "Pokedex\
\n\nSyntax : .pokedex <pokemon name>\
\nUsage : Gives Information About Given Pokemon.\
\n\nExample : .pokedex pikachu\
\nThis above syntax gives Information about Pikachu"
    }
)
