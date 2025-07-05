import asyncio
import discord
from discord.ext import commands
import random
import requests
import os
#from imagedet import get_class

description = "Bkwn prototype dsc bot #001"
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', description = description, intents = intents)

SAVE_DIR = "images"
os.makedirs(SAVE_DIR, exist_ok=True)

@bot.event
async def on_ready():
    print(f'Successfully logged in as {bot.user} / ID {bot.user.id}')
    print('-----See logs below-----')
 
@bot.command()
async def hello(ctx, member: discord.Member):
    """Greets the requesting user"""
    await ctx.send(f'Hello, {member.name}! {bot.user} here.')

@bot.command()
async def cmds(ctx):
    response = (
        "Prefix - $, command categories - **M**: basic functions, **F**: for fun, **U**: advanced utilities, **X**: experiments by creator\n"
        " \n"
        "All availale commands: \n"
        "$ping: (M) Checks network latency\n"
        "$coinflip: (F) Flips a virtual coin\n"
    )
    await ctx.send(response)

@bot.command()
async def ping(ctx):
    '''(M) Checks network latency'''
    fauxlat = random.randint(90,420)
    await ctx.send(f"Pong! Latency: {fauxlat}ms")

@bot.command()
async def gpt(ctx):
    '''(U) UNDER CONSTRUCTION'''
    await ctx.send("(This feature is under construction)")

@bot.command()
async def coinflip(ctx):
    '''(F) Flips a virtual coin'''
    flipped = random.choice('head','tail')
    await ctx.send(f'Coin flipped and landed on {flipped}')

@bot.command()
async def wordrep(ctx, times: int, content:str=""):
    '''(F) Repeats a word input by user's request'''
    for i in range(times):
        await ctx.send(content)


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''(F) Duck'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command(name="saveimg")
async def saveimg(ctx):
    '''(X) Forwards an image to the bot's database'''
    if not ctx.message.attachments:
        await ctx.send("No image")
        return

    for attachment in ctx.message.attachments:
        if attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            save_path = os.path.join(SAVE_DIR, attachment.filename)
            await attachment.save(save_path)
            await ctx.send(f"Image saved: `{attachment.filename}`")
            execution_path = os.getcwd()



# greenmission thing
@bot.command()
async def greenmission(ctx):
    response = (
        "**GREEN MISSION** / A secret project by this bot's maker... to keep the earth safe and healthy. Updates if planned. \n"
        " \n"
        "All availale commands: \n"
        "$gms_facts: Gives out a random fact about climate change \n"
        "$gms_tips: Gives out some tips on how to counter climate change \n"
        "$gms_quiz: Starts a simple 5-question quiz in the same topic \n"
    )
    await ctx.send(response)


# fakte
fshuffler = [
    {"fact": "An exhaustive review of peer-reviewed scientific literature reveals that over 99.9% of climate scientists concur that human activities are the primary driver of modern climate change. This level of consensus is comparable to the scientific agreement on the theory of plate tectonics or the existence of evolution."},
    {"fact": "Atmospheric carbon dioxide (CO2) concentrations have surpassed 420 parts per million (ppm), a level not seen in at least 2 million years. Before the Industrial Revolution, this figure was around 280 ppm. This surge is primarily due to the burning of fossil fuels like coal, oil, and natural gas."},
    {"fact": "Methane (CH4), another significant greenhouse gas, is more than 80 times more potent at trapping heat than CO2 over a 20-year period. Major sources of methane emissions include agriculture (particularly livestock), fossil fuel extraction, and landfills."},
    {"fact": "The last decade was the hottest in recorded history, and this trend is continuing. The Earth's average surface temperature has risen by approximately 1.2° Celsius (2.2° Fahrenheit) since the late 19th century, with the majority of this warming occurring in the last 50 years."},
    {"fact": "Global sea levels are rising at an accelerating rate. The primary contributors to this are the thermal expansion of seawater as it warms and the melting of glaciers and ice sheets. This poses a direct threat to coastal communities and ecosystems worldwide."},
    {"fact": "The oceans have absorbed about 30% of the anthropogenic carbon dioxide, leading to a 30% increase in the acidity of surface ocean waters. This process, known as ocean acidification, threatens the survival of many marine species, including corals and shellfish, by making it harder for them to build their skeletons and shells."},
    {"fact": "Climate change is increasing the frequency and intensity of extreme weather events such as heatwaves, droughts, heavy rainfall, and wildfires. These events have devastating consequences for agriculture, infrastructure, and human life."},
    {"fact": "The planet's ice is melting at an alarming rate. The Greenland and Antarctic ice sheets have been losing hundreds of billions of tons of ice per year, contributing significantly to sea-level rise. Glaciers in mountain ranges across the globe are also in rapid retreat."},
    {"fact": "Changes in temperature and precipitation patterns are disrupting agricultural yields and water availability. Some regions face increased risks of drought, while others experience more intense flooding, both of which can lead to food shortages and water crises."},
    {"fact": "Climate change is a major driver of biodiversity loss. As habitats change and become unsuitable, many plant and animal species are struggling to adapt or relocate, increasing the risk of extinction. The Intergovernmental Science-Policy Platform on Biodiversity and Ecosystem Services (IPBES) has warned that around 1 million animal and plant species are now threatened with extinction."},
    {"fact": "Climate change poses significant risks to human health. These include increased respiratory and cardiovascular diseases due to air pollution, the spread of infectious diseases as vectors like mosquitoes expand their range, and mental health impacts from displacement and the trauma of extreme weather events."},
    {"fact": "Rising sea levels, desertification, and an increase in the frequency of extreme weather events are already forcing people from their homes, creating a growing population of climate refugees."},
    {"fact": "Transitioning from fossil fuels to renewable energy sources like solar and wind power is one of the most critical actions needed to mitigate climate change. The cost of renewable energy technologies has fallen dramatically in recent years, making them increasingly competitive with fossil fuels."},
    {"fact": "Improving energy efficiency in buildings, transportation, and industries can significantly reduce greenhouse gas emissions. This includes measures such as better insulation, more efficient appliances, and the adoption of electric vehicles."},
    {"fact": "Protecting and restoring natural ecosystems, such as forests and wetlands, can play a vital role in absorbing and storing carbon. These nature-based solutions also provide numerous co-benefits for biodiversity and human well-being."}
]
@bot.command(name="gms_facts")
async def random_fact(ctx):
    yee = random.choice(fshuffler)
    await ctx.send(f"Random fact: {yee['fact']}")


# 222
tshuffler = [
    {"tip": "Turn off lights and unplug electronics when not in use to prevent energy drains."},
    {"tip": "Switch to home appliances with higher energy ratings, because these counterparts can last longer and be more efficient."},
    {"tip": "If your home is equipped with a thermostat or air conditioner, adjust it by a couple of degrees— lower in winter and higher in summer. Ensure your home is well-insulated to prevent energy waste."},
    {"tip": "Whenever possible, walk, cycle, or use public transport. These alternatives reduce emissions, ease traffic congestion, and improve public health."},
    {"tip": "If driving is necessary, carpool to reduce the number of vehicles on the road. For your next vehicle, consider an electric or hybrid model, which produces significantly fewer emissions over its lifetime."},
    {"tip": "Incorporating more plant-based meals into your diet is one of the most effective ways an individual can lower their environmental impact. Start by eating less meat-based dishes or by trying new vegetarian and vegan recipes."},
    {"tip": "Plan your meals, buy only what you need, and use your leftovers. Food that ends up in landfills decomposes and releases methane, a potent greenhouse gas."},
    {"tip": "Say no to disposable plastics like straws, cutlery, and water bottles. Opt for reusable alternatives."},
    {"tip": "Before throwing something away, consider if it can be repaired or given a new life."},
    {"tip": "Familiarize yourself with local recycling guidelines to ensure materials are processed properly."},
    {"tip": "A dripping tap can waste thousands of liters of water per year."},
    {"tip": "Take shorter showers, turn off the tap while brushing your teeth, and only run full loads in your dishwasher and washing machine."},
    {"tip": "If you are a homeowner, consider installing solar panels on your roof to generate your own clean energy."},
    {"tip": "Connect with local environmental groups or start a community initiative, such as a community garden, a repair cafe, or a local recycling program."},
]
@bot.command(name="gms_tips")
async def tips(ctx):
    yeet = random.choice(tshuffler)
    await ctx.send(f"Tip: {yeet['tip']}")

quiz_data = [
    {"question": "What is the main cause of climate change?", "answer": "greenhouse gas"},
    {"question": "Which gas is the biggest contributor to global warming?", "answer": "CO2"},
    {"question": "The sun can provide energy that is considered as renewable. What type of energy is this?", "answer": "solar"},
    {"question": "Farming of livestock can also generate one of the many greenhouse gases as its byproduct. Specifically, which gas is it?", "answer": "methane"},
    {"question": "How much is the **CURRENT EXACT** value of CO2 concentrations in the atmosphere, in ppm?", "answer": "428"},
]

# Function to start the quiz
@bot.command(name="gms_quiz")
async def start_quiz(ctx):
    score = 0
    random.shuffle(quiz_data)
    for idx, q_data in enumerate(quiz_data):
        question = q_data["question"]
        correct_answer = q_data["answer"]
        await ctx.send(f"Question {idx + 1}: {question}")
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        try:
            response = await bot.wait_for('message', timeout=15.0, check=check)
            if response.content.strip().lower() == correct_answer.lower():
                score += 1
                await ctx.send(f"Correct! Your current score is: {score}")
            else:
                await ctx.send(f"Incorrect! The correct answer was: {correct_answer}. Your current score is: {score}")
        except asyncio.TimeoutError:
            await ctx.send(f"Time's up! The correct answer was: {correct_answer}. Your score is: {score}")
    await ctx.send(f"Quiz Over! Your final score is: {score}/{len(quiz_data)}")














bot.run("TOKEN")