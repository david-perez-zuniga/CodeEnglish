from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.core.database import SessionLocal, engine
from app.models.md_Pages import Page
from app.models.md_Vocabulary import Vocabulary
from app.models.base import Base


vocabulary_data = [
    {"en": "Bucks", "es": "Dólares"},
    {"en": "(to) Dine", "es": "Cenar"},
    {"en": "(to) Grow up", "es": "Creer"},
    {"en": "(to) Mail", "es": "Enviar por correo"},
    {"en": "Manage", "es": "Administrar"},
    {"en": "Chinatown", "es": "Barrio chino"},
    {"en": "Chinese", "es": "Chino"},
    {"en": "Best known", "es": "Mejor conocido"},
    {"en": "Church", "es": "Iglesia"},
    {"en": "Fluent", "es": "Fluidez"},
    {"en": "Incidentally", "es": "A propósito"},
    {"en": "Management", "es": "Administración"},
    {"en": "Qualified", "es": "Calificado"},
    {"en": "From the bottom up", "es": "De abajo hacia arriba"},
    {"en": "Surrounded", "es": "Rodeado"},
    {"en": "Crime", "es": "Crimen"},
    {"en": "Branch", "es": "Sucursal"},
    {"en": "Service technician", "es": "Técnico en servicio"},
    {"en": "Dishwasher", "es": "Lavaplatos"},
    {"en": "Out of order", "es": "Descompuesto"},
    {"en": "Neighbor", "es": "Vecino"},
    {"en": "Garage", "es": "Garaje, taller"},
    {"en": "Brakes", "es": "Frenos"},
    {"en": "Repairs", "es": "Reparaciones"},
    {"en": "Maintenance", "es": "Mantenimiento"},
    {"en": "Equipment", "es": "Equipo"},
    {"en": "Appliances", "es": "Electrodomésticos"},
    {"en": "Budget", "es": "Presupuesto"},
    {"en": "Electrician", "es": "Electricista"},
    {"en": "Plumber", "es": "Plomero"},
    {"en": "Ways", "es": "Maneras, formas"},
    {"en": "Training", "es": "Entrenamiento"},
    {"en": "Skills", "es": "Habilidades"},
    {"en": "On the job training", "es": "Pago y entrenamiento"},
    {"en": "License", "es": "Licencia"},
    {"en": "White collar worker", "es": "Trabajador de oficina"},
    {"en": "Blue collar worker", "es": "Trabajador de la industria"},
    {"en": "Society", "es": "Sociedad"},
    {"en": "(to) Mean", "es": "Querer decir"},
    {"en": "(to) Seem", "es": "Parecer"},
    {"en": "(to) Hire", "es": "Emplear"},
    {"en": "(to) Dream", "es": "Soñar"},
    {"en": "(to) Include", "es": "Incluir"},
    {"en": "(to) Fill", "es": "Llenar, completar"},
    {"en": "(to) Supervise", "es": "Supervisar"},
    {"en": "(to) Carry out", "es": "Llevar a cabo"},
    {"en": "(to) Establish", "es": "Establecer"},
    {"en": "(to) Start out", "es": "Comenzar"},
    {"en": "(to) Rise", "es": "Levantarse, surgir"},
    {"en": "Once", "es": "Una vez"},
    {"en": "Headquarter", "es": "Casa matriz"},
    {"en": "Smallpox", "es": "Viruela"},
    {"en": "Agency", "es": "Agencia"},
    {"en": "Constant motion", "es": "Movimiento constante"},
    {"en": "Taxicab", "es": "Taxi"},
    {"en": "Bank teller", "es": "Cajero"},
    {"en": "Book keeper", "es": "Teneduría de libros"},
    {"en": "Insurance company", "es": "Compañía de seguros"},
    {"en": "Huge", "es": "Inmenso"},
    {"en": "Staff", "es": "Personal"},
    {"en": "Messenger", "es": "Mensajero"},
    {"en": "Through", "es": "A través de"},
    {"en": "Policies", "es": "Políticas de negocio"},
    {"en": "Financial matter", "es": "Asunto financiero"},
    {"en": "Manager", "es": "Gerente"},
    {"en": "(to) Produce", "es": "Producir"},
    {"en": "(to) Consist", "es": "Consistir"},
    {"en": "(to) Ship", "es": "Embarcar, Embarcarse"},
    {"en": "(to) Add", "es": "Agregar"},
    {"en": "(to) Belong", "es": "Pertenecer"},
    {"en": "(to) Cover", "es": "Cubrir"},
    {"en": "Of course", "es": "Por supuesto"},
    {"en": "Consumer product", "es": "Producto de consumo"},
    {"en": "Purchases", "es": "Compras"},
    {"en": "Lives", "es": "Vidas"},
    {"en": "Complex", "es": "Complejo"},
    {"en": "Piece", "es": "Pedazo, pieza"},
    {"en": "Machinery", "es": "Maquinaria"},
    {"en": "Spark plug", "es": "Chispero"},
    {"en": "Carburetor", "es": "Carburador"},
    {"en": "Assembly plant", "es": "Planta de ensamble"},
    {"en": "Conveyor belt", "es": "Faja de transportación"},
    {"en": "Frame", "es": "Marco, Armadura"},
    {"en": "Dealer", "es": "Distribuidor"},
    {"en": "Mass production", "es": "Producción en masa"},
    {"en": "Due", "es": "Debido"},
    {"en": "Availability", "es": "Disponibilidad"},
    {"en": "Wage", "es": "Salario por hora"},
    {"en": "(to) Exchange", "es": "Intercambiar"},
    {"en": "(to) Set up", "es": "Montar"},
    {"en": "(to) Display", "es": "Mostrar, exhibir"},
    {"en": "(to) Surround", "es": "Rodear"},
    {"en": "(to) Appear", "es": "Aparecer"}
]


async def seed_page_7():
    async with SessionLocal() as session:
        try:
            stmt = select(Page).where(Page.page_number == 7)
            result = await session.execute(stmt)
            page = result.scalar_one_or_none()

            if not page:
                page = Page(
                    page_number=7,
                    module_type="vocabulary",
                    subtitle="Basic Vocabulary - Page 7"
                )
                session.add(page)
                await session.flush()
                print(f"Created new Page with ID: {page.id}")
            else:
                print(f"Page 7 already exists with ID: {page.id}")

            existing_stmt = select(Vocabulary).where(Vocabulary.pages_id == page.id)
            existing_result = await session.execute(existing_stmt)
            existing_vocab = existing_result.scalars().all()
            
            if existing_vocab:
                print(f"Page 7 already has {len(existing_vocab)} vocabulary items. Skipping...")
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
            print(f"Successfully added {len(vocabulary_data)} vocabulary items to Page 7")

        except Exception as e:
            await session.rollback()
            print(f"Error during seeding: {e}")
            raise


if __name__ == "__main__":
    import asyncio
    asyncio.run(seed_page_7())