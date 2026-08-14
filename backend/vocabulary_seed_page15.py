from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.core.database import SessionLocal, engine
from app.models.md_Pages import Page
from app.models.md_Vocabulary import Vocabulary
from app.models.base import Base


vocabulary_data = [
    {"en": "(to) Differentiate", "es": "Diferenciar"},
    {"en": "(to) Perform", "es": "Actuar, Desempeñar, Ejercer"},
    {"en": "(to) Turn out", "es": "Resultar"},
    {"en": "(to) Analize", "es": "Analizar"},
    {"en": "(to) Work out", "es": "Resolver, Funcionar"},
    {"en": "Electronics", "es": "Electrónica"},
    {"en": "Transistor radios", "es": "Radio de transistores"},
    {"en": "Code", "es": "Código"},
    {"en": "In effect", "es": "En efecto"},
    {"en": "Switch", "es": "Interruptor"},
    {"en": "Altogether", "es": "Totalmente"},
    {"en": "Storage section", "es": "Sección de almacenaje"},
    {"en": "Payroll", "es": "Planilla, Nómina de sueldo"},
    {"en": "Device", "es": "Dispositivo"},
    {"en": "Input unit", "es": "Unidad por la cual se le suministra información a la computadora"},
    {"en": "Output unit", "es": "Unidad por la cual se obtiene la información de vuelta"},
    {"en": "Keyboard", "es": "Teclado"},
    {"en": "In advance", "es": "De antemano"},
    {"en": "Processing unit", "es": "Unidad de procesamiento"},
    {"en": "Request", "es": "Requerimiento"},
    {"en": "Tube", "es": "Tubo"},
    {"en": "Wires", "es": "Alambres, Cable, Telegrama"},
    {"en": "Trial", "es": "Prueba"},
    {"en": "Fear", "es": "Miedo, temor, pavor"},
    {"en": "Proper", "es": "Apropiado, correcto"},
    {"en": "Properly", "es": "Correctamente"},
    {"en": "Indeed", "es": "En realidad"},
    {"en": "Master", "es": "Maestro, amo"},
    {"en": "(to) Mate", "es": "Aparearse"},
    {"en": "(to) Consist", "es": "Consistir"},
    {"en": "(to) Bear", "es": "Parir, dar a luz"},
    {"en": "(to) Hunt", "es": "Cazar"},
    {"en": "(to) Support", "es": "Soportar, mantener"},
    {"en": "(to) Drown", "es": "Ahogarse"},
    {"en": "(to) Trap", "es": "Atrapar"},
    {"en": "(to) Bark", "es": "Ladrar"},
    {"en": "(to) Growl", "es": "Gruñir"},
    {"en": "(to) Communicate", "es": "Comunicarse"},
    {"en": "(to) Combine", "es": "Combinar"},
    {"en": "(to) Transmit", "es": "Trasmitir"},
    {"en": "(to) Determine", "es": "Determinar, Establecer"},
    {"en": "(to) Warn", "es": "Alertar"},
    {"en": "(to) Identify", "es": "Identificar"},
    {"en": "(to) Arouse", "es": "Levantar"},
    {"en": "Intelligence", "es": "Inteligencia"},
    {"en": "In the nick of time", "es": "A la hora indicada"},
    {"en": "Undoubtedly", "es": "Indudablemente"},
    {"en": "Exaggeration", "es": "Exageración"},
    {"en": "Utility companies", "es": "Compañía de agua, luz, teléfono"},
    {"en": "Income tax", "es": "Impuesto sobre los ingresos"},
    {"en": "Deduction", "es": "Deducción"},
    {"en": "Social security", "es": "Seguridad social"},
    {"en": "Record", "es": "Relación, cuenta"},
    {"en": "Mistake", "es": "Error"},
    {"en": "Charge", "es": "Cobro"},
    {"en": "Mailing label", "es": "Etiqueta de correo"},
    {"en": "Cash register", "es": "Caja registradora"},
    {"en": "Application", "es": "Aplicación"},
    {"en": "Diagnosis", "es": "Diagnosis"},
    {"en": "Treatment", "es": "Tratamiento"},
    {"en": "Symptoms", "es": "Síntomas"},
    {"en": "Illness", "es": "Enfermedad"},
    {"en": "Processes", "es": "Procesos"},
    {"en": "Unidentified flying object", "es": "Objeto volador no identificado"},
    {"en": "Military", "es": "Fuerza armada"},
    {"en": "Attached", "es": "Adherido, adjunto"},
    {"en": "Working class", "es": "La Clase obrera"},
    {"en": "Withdrawal", "es": "Retiro"},
    {"en": "(to) Jump", "es": "Saltar"},
    {"en": "(to) Welcome", "es": "Dar la bienvenida"},
    {"en": "(to) Train", "es": "Entrenar"},
    {"en": "(to) Adapt", "es": "Adaptar(se)"},
    {"en": "(to) Distinguish", "es": "Distinguir"},
    {"en": "(to) Bear", "es": "Parir dar la luz"},
    {"en": "(to) Draw", "es": "Aspirar, dibujar"},
    {"en": "(to) Slow down", "es": "Disminuir la velocidad"},
    {"en": "(to) Dive", "es": "Sumergirse"},
    {"en": "(to) Create", "es": "Crear"},
    {"en": "(to) Stand", "es": "Soportar"},
    {"en": "(to) Attempt", "es": "Intentar"},
    {"en": "(to) Bounce off", "es": "Rebotar"},
    {"en": "Sea", "es": "Mar"},
    {"en": "As though", "es": "Como si"},
    {"en": "Mediteranean", "es": "Mediterráneo"},
    {"en": "Friendly sight", "es": "Vista amistosa"},
    {"en": "Indeed", "es": "En realidad, en efecto"},
    {"en": "In fact", "es": "En realidad"},
    {"en": "Reputation", "es": "Reputación"},
    {"en": "Sociability", "es": "Sociabilidad"},
    {"en": "Imagination", "es": "Imaginación"},
    {"en": "Strong sense", "es": "Sentido fuerte"},
    {"en": "Calf", "es": "Becerro, ternera, cría"}
]


async def seed_page_15():
    async with SessionLocal() as session:
        try:
            stmt = select(Page).where(Page.page_number == 15)
            result = await session.execute(stmt)
            page = result.scalar_one_or_none()

            if not page:
                page = Page(
                    page_number=15,
                    module_type="vocabulary",
                    subtitle="Basic Vocabulary - Page 15"
                )
                session.add(page)
                await session.flush()
                print(f"Created new Page with ID: {page.id}")
            else:
                print(f"Page 15 already exists with ID: {page.id}")

            existing_stmt = select(Vocabulary).where(Vocabulary.pages_id == page.id)
            existing_result = await session.execute(existing_stmt)
            existing_vocab = existing_result.scalars().all()
            
            if existing_vocab:
                print(f"Page 15 already has {len(existing_vocab)} vocabulary items. Skipping...")
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
            print(f"Successfully added {len(vocabulary_data)} vocabulary items to Page 15")

        except Exception as e:
            await session.rollback()
            print(f"Error during seeding: {e}")
            raise


if __name__ == "__main__":
    import asyncio
    asyncio.run(seed_page_15())
