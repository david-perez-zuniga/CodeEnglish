from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.core.database import SessionLocal, engine
from app.models.md_Pages import Page
from app.models.md_Vocabulary import Vocabulary
from app.models.base import Base


vocabulary_data = [
    {"en": "(to)Pour", "es": "Vaciar, Llover a cántaros"},
    {"en": "(to)Explode", "es": "Explotar"},
    {"en": "(to)Float", "es": "Flotar"},
    {"en": "(to)Strike", "es": "Golpear"},
    {"en": "(to)Shake up", "es": "Sacudir, estremecerse"},
    {"en": "(to)Guide", "es": "Guiar"},
    {"en": "(to)Station", "es": "Estacionar(se)"},
    {"en": "(to)Fight", "es": "Pelear"},
    {"en": "(to)Surrender", "es": "Rendirse"},
    {"en": "(to)Argue", "es": "Argumentar, comentar"},
    {"en": "(to)Injure", "es": "Lastimar(se), lesionar"},
    {"en": "Sharp stab", "es": "Punzada aguda"},
    {"en": "Alive", "es": "Con vida"},
    {"en": "Steering wheel", "es": "Timón, volante"},
    {"en": "(to)Prepare", "es": "Preparar(se)"},
    {"en": "(to)Float ", "es": "Flotar"},
    {"en": "(to)Tie", "es": "Amarrar, atar"},
    {"en": "(to)Hold", "es": "Sostener, mantener"},
    {"en": "(to)Rise", "es": "Levantar(se)"},
    {"en": "(to)Faint", "es": "Desmayar(se)"},
    {"en": "(to)Throw away", "es": "Botar, desechar"},
    {"en": "(to)Wake", "es": "Despertar(se)"},
    {"en": "(to)Strike out", "es": "Dirigirse a"},
    {"en": "(to)Suffer", "es": "Sufrir"},
    {"en": "Completely", "es": "Completamente"},
    {"en": "Lieutenant", "es": "Teniente"},
    {"en": "Therefore", "es": "Por lo tanto"},
    {"en": "At once", "es": "Inmediatamente"},
    {"en": "Wood", "es": "Madera"},
    {"en": "Pairs", "es": "Pares"},
    {"en": "Lantern", "es": "Linterna"},
    {"en": "Strap", "es": "Faja, correa"},
    {"en": "Breaststroke", "es": "Nado de pecho"},
    {"en": "Fortunately", "es": "Afortunadamente"},
    {"en": "Coconuts", "es": "Cocos"},
    {"en": "Passage", "es": "Pasadizo"},
    {"en": "Rubber life belt", "es": "Salvar vidas"},
    {"en": "Reef", "es": "Arrecife"},
    {"en": "Beneath", "es": "Debajo"},
    {"en": "Far away", "es": "A lo lejos"},
    {"en": "Despite", "es": "A pesar de"},
    {"en": "Useless", "es": "Inútil"},
    {"en": "Current", "es": "Corriente, Actual"},
    {"en": "Weary", "es": "Cansado, Hostigado"},
    {"en": "Face to face", "es": "Cara a cara"},
    {"en": "Unconscious", "es": "Inconsciente"},
    {"en": "Event", "es": "Evento"},
    {"en": "Signal", "es": "Señal"},
    {"en": "Thirst", "es": "Sed"},
    {"en": "(to)Patrol", "es": "Rondar, patrulla"},
    {"en": "(to)Invade", "es": "Invadir"},
    {"en": "(to)Defend", "es": "Defender"},
    {"en": "(to)Remind", "es": "Recordarle"},
    {"en": "(to)Test", "es": "Someter a prueba"},
    {"en": "(to)Stretch out", "es": "Estirar, tumbar, reloj"},
    {"en": "(to)Locate", "es": "Localizar"},
    {"en": "Destroyer", "es": "Destructor"},
    {"en": "Strait", "es": "Estrecho(geográfico)"},
    {"en": "Sailors", "es": "Navegantes"},
    {"en": "Wide", "es": "Ancho"},
    {"en": "Extremely", "es": "Extremadamente"},
    {"en": "Navy", "es": "Marina de guerra"},
    {"en": "Machine gun", "es": "Ametralladora"},
    {"en": "Damage", "es": "Daño"},
    {"en": "Commander", "es": "Comandante"},
    {"en": "Pieces", "es": "Pedazos"},
    {"en": "Bottom", "es": "Abajo, fondo"},
    {"en": "Flames", "es": "Llamas"},
    {"en": "Half", "es": "Mitad"},
    {"en": "Rough", "es": "Turbulento(a)"},
    {"en": "Bodily", "es": "Corporalmente"},
    {"en": "Onto", "es": "En, sobre, encima"},
    {"en": "Period", "es": "Período"},
    {"en": "Companion", "es": "Compañero"},
    {"en": "Volcano", "es": "Volcán"},
    {"en": "Troop", "es": "Tropa"},
    {"en": "Camp", "es": "Campamento"},
    {"en": "Burns", "es": "Quemaduras"},
    {"en": "(to)Refuse", "es": "Rehusar"},
    {"en": "(to)Give up", "es": "Rendirse"},
    {"en": "(to)Turn over", "es": "Darse vuelta, volcarse"},
    {"en": "(to)Hold ", "es": "Sostenerse, sujetarse"},
    {"en": "(to)Hide", "es": "Esconder"},
    {"en": "(to)Scratch", "es": "Rayar, gravar, esculpir"},
    {"en": "(to)Border", "es": "Borde, lindar con"},
    {"en": "(to)Oppose", "es": "Oponerse a"},
    {"en": "(to)Wake up", "es": "Despertarse"},
    {"en": "(to)Please", "es": "Agradar, Complacer"},
    {"en": "(to)Place", "es": "Poner, Situar, Colocar"},
    {"en": "(to)Hug", "es": "Abrazar"},
    {"en": "(to)Jump", "es": "Saltar"},
    {"en": "(to)Guide ", "es": "Guiar"},
    {"en": "Even though", "es": "Aunque"},
    {"en": "Coconut milk", "es": "Leche de coco"},
    {"en": "Spirit", "es": "Espíritu"},
    {"en": "Hope", "es": "Esperanza"},
    {"en": "Although", "es": "Aunque"},
    {"en": "Weak", "es": "Débil"},
    {"en": "Wooden box", "es": "Caja de madera"},
    {"en": "Barrel", "es": "Barril"},
    {"en": "Upon", "es": "Sobre, encima"},
    {"en": "Strong wind", "es": "Viento fuerte"}
]


async def seed_page_13():
    async with SessionLocal() as session:
        try:
            stmt = select(Page).where(Page.page_number == 13)
            result = await session.execute(stmt)
            page = result.scalar_one_or_none()

            if not page:
                page = Page(
                    page_number=13,
                    module_type="vocabulary",
                    subtitle="Basic Vocabulary - Page 13"
                )
                session.add(page)
                await session.flush()
                print(f"Created new Page with ID: {page.id}")
            else:
                print(f"Page 13 already exists with ID: {page.id}")

            existing_stmt = select(Vocabulary).where(Vocabulary.pages_id == page.id)
            existing_result = await session.execute(existing_stmt)
            existing_vocab = existing_result.scalars().all()
            
            if existing_vocab:
                print(f"Page 13 already has {len(existing_vocab)} vocabulary items. Skipping...")
                print("If you want to re-seed, delete existing records first.")
                return

            for vocab_item in vocabulary_data:
                vocab = Vocabulary(
                    pages_id=page.id,
                    word=vocab_item["en"],
                    meaning=vocab_item["es"]
                )
                session.add(vocab)

            await session.commit()
            print(f"Successfully added {len(vocabulary_data)} vocabulary items to Page 13")

        except Exception as e:
            await session.rollback()
            print(f"Error during seeding: {e}")
            raise


if __name__ == "__main__":
    import asyncio
    asyncio.run(seed_page_13())
