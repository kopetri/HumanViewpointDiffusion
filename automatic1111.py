
args = [
    "sd_model", 
    "outpath_samples", 
    "outpath_grids", 
    "prompt_for_display", 
    "prompt", 
    "negative_prompt", 
    "styles", 
    "seed", 
    "subseed_strength", 
    "subseed", 
    "seed_resize_from_h", 
    "seed_resize_from_w", 
    "sampler_index", 
    "sampler_name", 
    "batch_size", 
    "n_iter", 
    "steps", 
    "cfg_scale", 
    "width", 
    "height", 
    "restore_faces", 
    "tiling", 
    "do_not_save_samples", 
    "do_not_save_grid"
]

styles = [
    "photo-realistic urban cityscape at dawn with detailed architecture and city lights.",
    "cinematic shot of a mysterious forest with dense foliage and soft, atmospheric lighting.",
    "highly detailed, lifelike portrait capturing facial features and expressions.",
    "photo-realistic underwater scene with vibrant coral reefs and exotic marine life.",
    "cinematic depiction of a medieval fantasy castle with dramatic lighting and epic scale.",
    "photo-realistic still life composition of an elegant bouquet of flowers.",
    "highly realistic architectural visualization of a modern, luxurious penthouse interior.",
    "cinematic image of a spaceship in a futuristic, sci-fi setting with intricate details.",
    "photo-realistic wildlife scene showcasing animals in their natural habitat.",
    "detailed and lifelike depiction of an antique car, highlighting its fine craftsmanship.",
    "cinematic battle scene from a historical period, complete with period-accurate costumes and settings.",
    "highly realistic macro photograph capturing intricate textures of a natural object.",
    "photo-realistic winter landscape with snow-covered mountains and serene atmosphere.",
    "cinematic shot of an alien world with bizarre landscapes and otherworldly lighting.",
    "detailed and lifelike image of a delectable gourmet meal with vibrant colors.",
    "photo-realistic seascape with rolling waves, a sandy beach, and a colorful sunset.",
    "cinematic scene from a film noir movie with dramatic shadows and vintage aesthetics.",
    "highly detailed architectural rendering of a historic, ancient temple complex.",
    "photo-realistic portrait of a famous historical figure with attention to historical accuracy.",
    "cinematic image of an ancient, overgrown ruin in a lush jungle setting.",
    "highly realistic close-up of a scientific laboratory with intricate equipment and lighting.",
    "photo-realistic depiction of a bustling market scene in a foreign cultural setting.",
    "cinematic shot of a post-apocalyptic cityscape with destroyed buildings and eerie atmosphere.",
    "highly detailed image of a futuristic, high-tech laboratory with holographic interfaces.",
    "photo-realistic wildlife scene showcasing a majestic predator in its natural environment.",
    "cinematic depiction of an alien invasion with advanced spacecraft and dramatic effects.",
    "highly realistic architectural visualization of a serene, modern waterfront residence.",
    "photo-realistic still life composition of a vintage collection of books and antique items.",
    "cinematic scene from a classic Western movie with cowboys and a rugged desert backdrop.",
    "detailed image of a sci-fi space station with advanced technology and a sense of scale.",
    "highly realistic depiction of a classic, elegant ballroom from a bygone era.",
    "cinematic image of a post-apocalyptic wasteland with harsh landscapes and desolation.",
    "photo-realistic seascape with a rocky coastline, crashing waves, and a dramatic sky.",
    "detailed image of a bustling, futuristic cityscape with flying cars and neon lights.",
    "highly realistic portrait of a famous artist, capturing their unique personality.",
    "cinematic depiction of an epic fantasy battle with mythical creatures and magic.",
    "photo-realistic urban cityscape at night with stunning skyscrapers and city lights.",
    "highly detailed architectural rendering of an ancient, mystical temple ruins.",
    "cinematic image of a time-travel machine with intricate gears and mystical elements.",
    "photo-realistic still life composition of a lavish banquet table with exquisite cuisine.",
    "detailed and lifelike image of an exotic tropical rainforest with diverse flora and fauna.",
    "cinematic shot of a futuristic, cyberpunk city with towering skyscrapers and neon signs.",
    "highly realistic architectural visualization of a contemporary, minimalist art gallery.",
    "photo-realistic wildlife scene featuring an intimate moment between parent and offspring.",
    "cinematic depiction of a Viking raid on a medieval coastal village with historical accuracy.",
    "highly detailed close-up of a classic, vintage automobile's intricate details.",
    "photo-realistic winter landscape with a frozen lake, snow-covered trees, and a serene atmosphere.",
    "cinematic scene from a post-apocalyptic, dystopian future with gritty urban decay.",
    "highly realistic macro photograph of a delicate, colorful butterfly resting on a flower.",
    "detailed image of a cutting-edge research laboratory with scientists at work.",
    "cinematic image of a fantasy realm with mythical creatures, majestic castles, and enchanting landscapes.",
    "photo-realistic seascape with a tranquil, sunlit beach and crystal-clear waters.",
    "highly detailed architectural rendering of an iconic, historical landmark.",
    "cinematic scene from a classic detective noir film with a private investigator and mysterious atmosphere.",
    "highly realistic portrait of a famous scientist, capturing their intellectual essence.",
    "photo-realistic depiction of an ancient, mystical forest with ancient ruins and enchanted wildlife.",
    "cinematic image of a high-tech, futuristic cityscape with advanced transportation and dazzling lights.",
    "detailed and lifelike image of an opulent, ornate ballroom from a royal palace.",
    "photo-realistic urban cityscape during a vibrant sunset with stunning colors and atmospheric effects.",
    "cinematic shot of a serene, tranquil Zen garden with meticulously arranged elements.",
    "highly realistic architectural visualization of a cutting-edge, contemporary skyscraper.",
    "detailed image of a group of majestic wild animals on the savannah in their natural habitat.",
    "cinematic depiction of a thrilling space battle with futuristic spacecraft and dynamic action.",
    "photo-realistic still life composition of an exquisite, vintage collection of fine wines and glassware.",
    "highly detailed scene of an ancient, mythological battlefield with epic battles and legendary figures.",
    "cinematic image of an advanced, utopian city of the future with sleek, sustainable architecture.",
    "highly realistic close-up of an intricate, mechanical clock with gears and cogs.",
    "photo-realistic winter landscape with a charming, snow-covered village and cozy cottages.",
    "cinematic scene from a cyberpunk dystopia with towering skyscrapers, neon lights, and futuristic technology.",
    "detailed image of a bustling, lively carnival with rides, games, and colorful lights.",
    "highly realistic architectural rendering of an ancient, majestic cathedral with stunning Gothic architecture.",
    "cinematic depiction of a medieval jousting tournament with knights in shining armor and a cheering crowd.",
    "photo-realistic urban cityscape at twilight with a blend of natural and artificial light sources.",
    "detailed image of an intricate, magical library filled with ancient tomes and mystical artifacts.",
    "cinematic image of an otherworldly, extraterrestrial landscape with strange creatures and alien flora.",
    "highly realistic still life composition of a lavish, opulent banquet table with sumptuous cuisine.",
    "photo-realistic depiction of a serene, coastal lighthouse overlooking a peaceful seascape.",
    "detailed image of a lively, vibrant market square with street vendors and bustling activity.",
    "cinematic scene from a post-apocalyptic wasteland with a lone wanderer and a sense of survival.",
    "highly realistic architectural visualization of a modern, eco-friendly, sustainable building.",
    "photo-realistic wildlife scene showcasing a mesmerizing courtship display of exotic birds.",
    "cinematic depiction of a Roman gladiatorial arena with fierce combat and a roaring crowd.",
    "detailed and lifelike image of a vintage, classic motorcycle with intricate mechanical details.",
    "photo-realistic winter landscape with a frozen river, snow-covered forests, and serene quietude.",
    "cinematic shot of an ancient, mystical library with hidden secrets and ancient manuscripts.",
    "highly realistic macro photograph of a stunning, delicate dragonfly perched on a water lily.",
    "detailed image of a futuristic, high-tech laboratory with advanced equipment and scientific experiments.",
    "cinematic image of a prehistoric, primeval world with massive dinosaurs and lush, ancient vegetation.",
    "photo-realistic seascape with a breathtaking coastal cliff, dramatic waves, and a radiant sunset.",
    "highly detailed architectural rendering of a futuristic, otherworldly city with gravity-defying architecture.",
    "cinematic scene from a classic Hollywood film noir with detectives, femme fatales, and suspenseful intrigue.",
    "photo-realistic portrait of a renowned musician, capturing their unique musical essence.",
    "cinematic depiction of a mythical, enchanted forest with magical creatures and hidden wonders.",
    "highly realistic urban cityscape at dusk with shimmering skyscrapers and reflections on a rain-slicked street.",
    "detailed image of an elaborate, historic ballroom with opulent chandeliers and grandeur.",
]


class JobGenerator:
    def __init__(self, job_file, *args, **kwargs) -> None:
        self.output = job_file
        self.args = args
        self.kwargs = kwargs
        
    def generate(self, append=True):
        mode = "a" if append else "w"
        with open(self.output, mode) as txtfile:
            command = []
            for key, value in self.kwargs.items():
                if isinstance(value, str):
                    if value:
                        command.append(f"--{key} '{value}'")
                else:
                    command.append(f"--{key} {value}")
            command = " ".join(command)
            print(command)
            txtfile.write(f"{command}\n")
    
if __name__ == "__main__":
    from pathlib import Path
    modelnet28categories = [d.stem for d in Path("E:/data/modelnet28").glob("*") if d.is_dir()][0:1]
    for cat in modelnet28categories:
        for style in styles:
            g = JobGenerator("jobs.txt", 
                            prompt=f"{cat.replace('_', ' ')}, {style}",
                            n_iter=1, # number of images,
                            steps=5, # sample steps
                            sampler_name="DPM++ 2M Karras",
                            batch_size=8,
                            seed=1337,
                            outpath_samples=f"E:/projects/HumanViewpointDiffusion/test/automatic1111/{cat}",
                            cfg_scale=7)
            g.generate(append=True)