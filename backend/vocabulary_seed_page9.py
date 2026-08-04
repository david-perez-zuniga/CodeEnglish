from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.core.database import SessionLocal, engine
from app.models.md_Pages import Page
from app.models.md_Vocabulary import Vocabulary
from app.models.base import Base


vocabulary_data = [
    {"en": "Unpaved", "es": "Sin Pavimentar"},
    {"en": "Accomodations", "es": "Comodidades, Alojamiento"},
    {"en": "Along", "es": "A lo largo de"},
    {"en": "Storms", "es": "Tormentas"},
    {"en": "Development", "es": "Desarrollos"},
    {"en": "(to) Qualify", "es": "Calificar"},
    {"en": "Medicine", "es": "Medicina"},
    {"en": "Law", "es": "Leyes"},
    {"en": "Theology", "es": "Teología"},
    {"en": "Are known", "es": "Son conocidas"},
    {"en": "Profession", "es": "Profesión"},
    {"en": "Level", "es": "Nivel"},
    {"en": "Beyond", "es": "Mas allá"},
    {"en": "Even", "es": "Aun"},
    {"en": "Intern", "es": "Interno"},
    {"en": "Although", "es": "Aunque"},
    {"en": "Teaching", "es": "Magisterio, Docente"},
    {"en": "Occupation", "es": "Ocupación"},
    {"en": "Amount", "es": "Cantidad"},
    {"en": "Because of", "es": "Debido a"},
    {"en": "Barber", "es": "Barbero"},
    {"en": "Craftsmen", "es": "Artesanos"},
    {"en": "Developed", "es": "Desarrollado"},
    {"en": "Within", "es": "Dentro de"},
    {"en": "Civil engineering", "es": "Ingeniería civil"},
    {"en": "Dams", "es": "Presas"},
    {"en": "Bridge", "es": "Puente"},
    {"en": "Either... or", "es": "O... o"},
    {"en": "Certified public accountant", "es": "Contador público autorizado"},
    {"en": "Reward", "es": "Recompensa"},
    {"en": "Living", "es": "Vida"},
    {"en": "Independence", "es": "Independencia"},
    {"en": "Advise", "es": "Consejo"},
    {"en": "Effort", "es": "Esfuerzo, obra, trabajo"},
    {"en": "Status", "es": "Nivel de vida"},
    {"en": "(to) Encourage", "es": "Animar, alentar"},
    {"en": "(to) Come out", "es": "Salir"},
    {"en": "(to) Consist", "es": "Consistir"},
    {"en": "(to) Deal with", "es": "Tratar con"},
    {"en": "(to) Treat", "es": "Tratar"},
    {"en": "(to) Administer", "es": "Administrar"},
    {"en": "(to) Get away", "es": "Escapar, huir"},
    {"en": "(to) Bend", "es": "Doblar"},
    {"en": "(to) Bend over", "es": "Agacharse"},
    {"en": "(to) Put off", "es": "Posponer"},
    {"en": "Medicine", "es": "Medicina"},
    {"en": "In fact", "es": "En realidad"},
    {"en": "Orderlies", "es": "Ordenanzas"},
    {"en": "Annual", "es": "Anual"},
    {"en": "Average", "es": "Promedio"},
    {"en": "Check up", "es": "Chequeo"},
    {"en": "Steamship", "es": "Barco de vapor"},
    {"en": "Against", "es": "En contra de"},
    {"en": "Railroad", "es": "Vía ferroviaria"},
    {"en": "Fare", "es": "Tarifa"},
    {"en": "Seaside", "es": "Área cerca del mar"},
    {"en": "Tourism", "es": "Turismo"},
    {"en": "(to) Represent", "es": "Representar"},
    {"en": "(to) Divide", "es": "Dividir"},
    {"en": "(to) Decide", "es": "Decidir"},
    {"en": "(to) Collect", "es": "Recoger"},
    {"en": "(to) Handle", "es": "Manejar, llevar"},
    {"en": "(to) Appoint", "es": "Nombrar"},
    {"en": "(to) Fire", "es": "Despedir"},
    {"en": "Above", "es": "Sobre, encima, arriba"},
    {"en": "The entire nation", "es": "Toda la nación"},
    {"en": "Century", "es": "Siglo"},
    {"en": "Branch", "es": "Rama, sucursal"},
    {"en": "Legislative", "es": "Legislativo"},
    {"en": "Laws", "es": "Leyes"},
    {"en": "Judicial", "es": "Judicial"},
    {"en": "Judge", "es": "Juez"},
    {"en": "Court", "es": "Corte"},
    {"en": "Executive", "es": "Ejecutivo"},
    {"en": "Commander in chief", "es": "Comandante en jefe"},
    {"en": "Armed forces", "es": "Fuerzas armadas"},
    {"en": "Army", "es": "Ejército"},
    {"en": "Navy", "es": "Marina"},
    {"en": "Air force", "es": "Fuerza aérea"},
    {"en": "Huge", "es": "Inmenso"},
    {"en": "Bureaucracy", "es": "Burocracia"},
    {"en": "Bureau", "es": "Departamento, oficina"},
    {"en": "Taxes", "es": "Impuestos"},
    {"en": "Foreign affairs", "es": "Asuntos extranjeros"},
    {"en": "Applicant", "es": "Aspirante"},
    {"en": "Servant", "es": "Servidor"},
    {"en": "Merit", "es": "Mérito"},
    {"en": "Below", "es": "Abajo, debajo"},
    {"en": "Flunked out", "es": "Reprobar"},
    {"en": "(to) Carry out", "es": "Llevar a cabo, Cumplir"},
    {"en": "(to) Transfer", "es": "Transferir"},
    {"en": "(to) Encounter", "es": "Encontrar"},
    {"en": "Eyes", "es": "Ojos"},
    {"en": "Lungs", "es": "Pulmones"},
    {"en": "Illness", "es": "Enfermedad"},
    {"en": "Reason", "es": "Razón"},
    {"en": "Pediatrician", "es": "Pediatra"},
    {"en": "Gynecologist", "es": "Ginecólogo"},
    {"en": "Ophthalmologist", "es": "Oftalmólogo"},
    {"en": "Surgeon", "es": "Cirujano"},
    {"en": "Surgery", "es": "Cirugía"},
    {"en": "Drug", "es": "droga"}
]


async def seed_page_9():
    async with SessionLocal() as session:
        try:
            stmt = select(Page).where(Page.page_number == 9)
            result = await session.execute(stmt)
            page = result.scalar_one_or_none()

            if not page:
                page = Page(
                    page_number=9,
                    module_type="vocabulary",
                    subtitle="Basic Vocabulary - Page 9"
                )
                session.add(page)
                await session.flush()
                print(f"Created new Page with ID: {page.id}")
            else:
                print(f"Page 9 already exists with ID: {page.id}")

            existing_stmt = select(Vocabulary).where(Vocabulary.pages_id == page.id)
            existing_result = await session.execute(existing_stmt)
            existing_vocab = existing_result.scalars().all()
            
            if existing_vocab:
                print(f"Page 9 already has {len(existing_vocab)} vocabulary items. Skipping...")
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
            print(f"Successfully added {len(vocabulary_data)} vocabulary items to Page 9")

        except Exception as e:
            await session.rollback()
            print(f"Error during seeding: {e}")
            raise


if __name__ == "__main__":
    import asyncio
    asyncio.run(seed_page_9())
