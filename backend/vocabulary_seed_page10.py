from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.core.database import SessionLocal, engine
from app.models.md_Pages import Page
from app.models.md_Vocabulary import Vocabulary
from app.models.base import Base


vocabulary_data = [
    {"en": "Patient", "es": "Paciente"},
    {"en": "Pain", "es": "Dolor"},
    {"en": "Annually", "es": "Anualmente"},
    {"en": "Remedy", "es": "Remedio"},
    {"en": "Prescription", "es": "Prescripción"},
    {"en": "Over the counter", "es": "Sin prescripción médica"},
    {"en": "Vitamin", "es": "Vitamina"},
    {"en": "Properly", "es": "Propiamente"},
    {"en": "Pillars", "es": "Columnas"},
    {"en": "(to)Keep on", "es": "Continuar"},
    {"en": "(to)Grow", "es": "Crecer"},
    {"en": "(to)Feed", "es": "Alimentar"},
    {"en": "(to)Export", "es": "Exportar"},
    {"en": "(to)Raise", "es": "Cultivar, criar"},
    {"en": "(to)Provide", "es": "Proveer"},
    {"en": "(to)Turn out", "es": "Producir"},
    {"en": "Population", "es": "Población"},
    {"en": "Everyone", "es": "Todo el mundo"},
    {"en": "Lucky", "es": "Con suerte"},
    {"en": "Variety", "es": "Variedad"},
    {"en": "Climates", "es": "Climas"},
    {"en": "Suitable", "es": "Disponible"},
    {"en": "Wheat", "es": "Trigo"},
    {"en": "Corn", "es": "Maíz"},
    {"en": "Tons", "es": "Toneladas"},
    {"en": "In turn", "es": "En cambio"},
    {"en": "Warm", "es": "Caluroso"},
    {"en": "Damp", "es": "Húmedo"},
    {"en": "Cotton", "es": "Algodón"},
    {"en": "Rice", "es": "Arroz"},
    {"en": "Sugar", "es": "Azúcar"},
    {"en": "Vegetables", "es": "Vegetales"},
    {"en": "Famous", "es": "Famoso"},
    {"en": "Grapefruit", "es": "Toronja"},
    {"en": "On the other hand", "es": "Por el contrario"},
    {"en": "By means of", "es": "Por medio de"},
    {"en": "Irrigation", "es": "Irrigación"},
    {"en": "Grapes", "es": "Uvas"},
    {"en": "(to)Consist", "es": "Consistir"},
    {"en": "(to)Differ", "es": "Diferir"},
    {"en": "(to)Charge", "es": "Cobrar"},
    {"en": "Task", "es": "Tarea"},
    {"en": "Rather than", "es": "En vez de"},
    {"en": "Regulation", "es": "Norma, regla"},
    {"en": "County", "es": "Condado"},
    {"en": "In spite of", "es": "A pesar de"},
    {"en": "Elementary school", "es": "Primaria"},
    {"en": "Grade", "es": "Grado"},
    {"en": "Locality", "es": "Localidad"},
    {"en": "In addition", "es": "Además"},
    {"en": "Kindergarten", "es": "Jardín de infantil"},
    {"en": "Day care center", "es": "C.d.i"},
    {"en": "Compulsory", "es": "Obligado, a la fuerza"},
    {"en": "Curriculum", "es": "Currículum"},
    {"en": "Unequal", "es": "Desigual"},
    {"en": "Pupil", "es": "Pupilo"},
    {"en": "Religious", "es": "Religioso"},
    {"en": "Free", "es": "Gratis"},
    {"en": "Fee", "es": "Honorario, cuota"},
    {"en": "Branches", "es": "Sucursales, ramas"},
    {"en": "All over", "es": "Todo"},
    {"en": "In fact", "es": "En realidad"},
    {"en": "(to)Define", "es": "Definir"},
    {"en": "(to)Appeal", "es": "Atraer, interesar"},
    {"en": "(to)Keep up with", "es": "Mantenerse al tanto"},
    {"en": "(to)Disappear", "es": "Desaparecer"},
    {"en": "(to)Remain", "es": "Permanecer"},
    {"en": "(to)Show off", "es": "Exhibirse"},
    {"en": "(to)Hide", "es": "Esconder"},
    {"en": "Broadly", "es": "Ampliasmente"},
    {"en": "Painting", "es": "Pintura"},
    {"en": "Varieed", "es": "Artesanías"},
    {"en": "Crafts", "es": "Artesanías"},
    {"en": "Teenagers", "es": "Adolescentes"},
    {"en": "Adventure", "es": "Aventura"},
    {"en": "Plays", "es": "Obras de teatro"},
    {"en": "Wines", "es": "Vinos"},
    {"en": "Cattle", "es": "Ganado"},
    {"en": "Beef", "es": "Carne"},
    {"en": "Ripe", "es": "Maduro(a)"},
    {"en": "Owner", "es": "Propietario"},
    {"en": "(to)Sail", "es": "Navegar"},
    {"en": "(to)Break through", "es": "Abrir paso"},
    {"en": "(to)Reach", "es": "Alcanzar"},
    {"en": "(to)Spread out", "es": "Extenderse"},
    {"en": "(to)Colonize", "es": "Colonizar"},
    {"en": "(to)Explore", "es": "Explorar"},
    {"en": "(to)Turn out", "es": "Resultar"},
    {"en": "(to)Lie", "es": "Yacer"},
    {"en": "(to)Send back", "es": "Devolver, regresar"},
    {"en": "(to)Orbit", "es": "Orbitar"},
    {"en": "(to)Support", "es": "Soportar"},
    {"en": "(to)Solve", "es": "Resolver"},
    {"en": "(to)Cover", "es": "Cubrir"},
    {"en": "(to)Accompany", "es": "Acompañar"},
    {"en": "(to)Involve", "es": "Involucrar"},
    {"en": "(to)Turn back", "es": "Retornar"},
    {"en": "(to)Kill off", "es": "Matar"},
    {"en": "(to)Conquer", "es": "Conquistar"},
    {"en": "Oceans", "es": "Océanos"},
    {"en": "Knowledge", "es": "Conocimientos"},
    {"en": "Shore", "es": "Costa"},
    {"en": "Portuguese", "es": "Portugués"}
]


async def seed_page_10():
    async with SessionLocal() as session:
        try:
            stmt = select(Page).where(Page.page_number == 10)
            result = await session.execute(stmt)
            page = result.scalar_one_or_none()

            if not page:
                page = Page(
                    page_number=10,
                    module_type="vocabulary",
                    subtitle="Basic Vocabulary - Page 10"
                )
                session.add(page)
                await session.flush()
                print(f"Created new Page with ID: {page.id}")
            else:
                print(f"Page 10 already exists with ID: {page.id}")

            existing_stmt = select(Vocabulary).where(Vocabulary.pages_id == page.id)
            existing_result = await session.execute(existing_stmt)
            existing_vocab = existing_result.scalars().all()
            
            if existing_vocab:
                print(f"Page 10 already has {len(existing_vocab)} vocabulary items. Skipping...")
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
            print(f"Successfully added {len(vocabulary_data)} vocabulary items to Page 10")

        except Exception as e:
            await session.rollback()
            print(f"Error during seeding: {e}")
            raise


if __name__ == "__main__":
    import asyncio
    asyncio.run(seed_page_10())
