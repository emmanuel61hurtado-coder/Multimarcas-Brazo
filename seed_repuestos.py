from app import create_app, db
from app.models.repuesto import Repuesto

app = create_app()

repuestos_data = [
    # 🛢️ ACEITES Y LUBRICANTES (15)
    ("Aceite 100% Sintético 7100 10W40 4T", "Lubricantes", "Motul", 55000, 20, "Aceite premium para alto rendimiento y protección extrema."),
    ("Aceite Semisintético 5100 15W50", "Lubricantes", "Motul", 42000, 30, "Protección estándar ideal para motos urbanas."),
    ("Aceite Mineral 3000 20W50", "Lubricantes", "Motul", 32000, 25, "Aceite mineral para uso tradicional."),
    ("Aceite Racing 4T 10W40", "Lubricantes", "Castrol", 48000, 15, "Aceite Castrol Power 1 Racing."),
    ("Aceite Actevo 20W50 4T", "Lubricantes", "Castrol", 35000, 20, "Protección continua en todo momento."),
    ("Aceite 2T Sintético Kart", "Lubricantes", "Motul", 45000, 12, "Aceite 2T de alta performance para motores de dos tiempos."),
    ("Aceite para Horquillas 10W", "Lubricantes", "Motul", 40000, 10, "Fork Oil para suspensión delantera."),
    ("Aceite para Horquillas 20W", "Lubricantes", "Motul", 42000, 8, "Aceite viscoso para suspensión deportiva."),
    ("Lubricante de Cadena C2", "Lubricantes", "Motul", 38000, 15, "Spray lubricante para cadenas off-road y urbanas."),
    ("Grasa de Litio Multipropósito", "Lubricantes", "SKF", 18000, 10, "Grasa para rodamientos y piezas móviles."),
    ("Grasa para Rodamientos de Rueda", "Lubricantes", "SKF", 22000, 12, "Grasa consistente para balineras."),
    ("Grasa de Cobre Antigripante", "Lubricantes", "Loctite", 35000, 8, "Pasta de cobre para frenos y bujes."),
    ("WD-40 Multipropósito", "Lubricantes", "WD-40", 22000, 25, "Spray penetrante, lubricante y anticorrosivo."),
    ("Lubricante de Silicona en Spray", "Lubricantes", "WD-40", 25000, 15, "Lubricante para partes plásticas y gomas."),
    ("Aceite de Transmisión 75W90 GL5", "Lubricantes", "Castrol", 38000, 10, "Aceite para caja de cambios."),

    # 🛑 FRENOS (12)
    ("Pastillas de Freno Delanteras Sinterizadas", "Frenos", "Brembo", 85000, 10, "Máximo poder de frenado para calle/pista."),
    ("Pastillas de Freno Traseras Orgánicas", "Frenos", "EBC", 45000, 15, "Larga duración y cuidado del disco."),
    ("Bandas de Freno Traseras", "Frenos", "Ichiban", 25000, 20, "Zapatas de freno genéricas de alta calidad."),
    ("Pastillas de Freno Genéricas", "Frenos", "Revo", 18000, 30, "Pastillas económicas para uso diario."),
    ("Disco de Freno Delantero Flotante", "Frenos", "OEM Yamaha", 120000, 5, "Disco flotante original."),
    ("Disco de Freno Trasero", "Frenos", "OEM Honda", 95000, 5, "Disco trasero original."),
    ("Línea de Freno Blindada", "Frenos", "Venom", 65000, 8, "Manguera acerada para mayor precisión."),
    ("Bomba de Freno Delantera Completa", "Frenos", "Nissin", 150000, 3, "Bomba de freno hidráulica completa."),
    ("Bomba de Freno Trasera", "Frenos", "OEM", 85000, 4, "Bomba de freno trasera original."),
    ("Kit de Reparación de Bomba de Freno", "Frenos", "OEM", 25000, 8, "Kit con empaques y pistones."),
    ("Líquido de Frenos DOT 4", "Frenos", "Motul", 25000, 15, "Líquido de frenos de alto punto de ebullición."),
    ("Líquido de Frenos DOT 5.1", "Frenos", "Castrol", 35000, 10, "Líquido sintético de altísimo rendimiento."),

    # ⚙️ TRANSMISIÓN (12)
    ("Kit de Arrastre O-Ring D.I.D", "Transmisión", "DID", 180000, 5, "Cadena reforzada, plato y piñón. Larga vida."),
    ("Kit de Arrastre Estándar", "Transmisión", "Choho", 85000, 12, "Kit de cadena sin O-Ring económico."),
    ("Kit de Arrastre Premium", "Transmisión", "Renthal", 220000, 3, "Kit de aluminio ultra ligero para competición."),
    ("Cadena Reforzada 428H", "Transmisión", "KMC", 45000, 15, "Cadena sola paso 428."),
    ("Cadena O-Ring 520", "Transmisión", "DID", 130000, 5, "Cadena reforzada para motos de alto cilindraje."),
    ("Piñón de Salida 14T", "Transmisión", "JT Sprockets", 25000, 10, "Piñón delantero de acero."),
    ("Piñón de Salida 15T", "Transmisión", "JT Sprockets", 25000, 10, "Piñón delantero de acero 15 dientes."),
    ("Plato Trasero 42T", "Transmisión", "JT Sprockets", 55000, 8, "Plato de acero al carbono."),
    ("Plato Trasero 46T", "Transmisión", "JT Sprockets", 55000, 8, "Plato trasero de acero 46 dientes."),
    ("Seguro de Cadena", "Transmisión", "Genérico", 5000, 50, "Pin de seguridad para cadenas."),
    ("Tensores de Cadena (Par)", "Transmisión", "OEM", 18000, 15, "Tensores de caucho para basculante."),
    ("Kit de Arrastre 520 Conversion", "Transmisión", "Renthal", 280000, 2, "Kit paso 520 de alto rendimiento."),

    # ⚡ SISTEMA ELÉCTRICO (20)
    ("Bujía Estándar CPR8EA-9", "Eléctrico", "NGK", 15000, 40, "Bujía original de cobre para múltiples modelos."),
    ("Bujía Iridium CR9EIX", "Eléctrico", "NGK", 45000, 20, "Mejor chispa, menor consumo y larga vida útil."),
    ("Bujía de Calor CR7E", "Eléctrico", "NGK", 12000, 30, "Bujía de cobre estándar."),
    ("Bujía Iridium CR8EIX", "Eléctrico", "NGK", 45000, 15, "Bujía de iridio de alto rendimiento."),
    ("Batería YTZ7S Libre de Mantenimiento", "Eléctrico", "Yuasa", 150000, 8, "Batería sellada 12V 6Ah."),
    ("Batería de Gel 12V 7Ah", "Eléctrico", "MAG", 95000, 12, "Batería económica de gel."),
    ("Batería YTX9-BS Sellada", "Eléctrico", "Yuasa", 180000, 5, "Batería de alto amperaje 12V 8Ah."),
    ("Bombillo Farola LED H4", "Eléctrico", "Philips", 55000, 15, "Luz blanca 6000k de alta potencia."),
    ("Bombillo Halógeno H4", "Eléctrico", "Osram", 20000, 20, "Bombillo original luz amarilla."),
    ("Bombillo LED H7", "Eléctrico", "Philips", 65000, 10, "Bombillo LED de alta luminosidad."),
    ("Bombillo Direccional 12V 10W", "Eléctrico", "Genérico", 3000, 50, "Bombillo tradicional muela."),
    ("Bombillo Luz de Freno LED", "Eléctrico", "Genérico", 8000, 20, "Bombillo LED rojo para luz trasera."),
    ("Estator/Bobina de Encendido", "Eléctrico", "OEM", 130000, 4, "Corona de bobinas para sistema de carga."),
    ("CDI Racing Sin Límite", "Eléctrico", "BRT", 95000, 5, "CDI sin limitador de RPM."),
    ("CDI Original", "Eléctrico", "OEM", 120000, 4, "Módulo de encendido original."),
    ("Relé de Arranque (Marano)", "Eléctrico", "OEM", 35000, 10, "Chancho o automático de arranque."),
    ("Motor de Arranque Completo", "Eléctrico", "OEM", 180000, 3, "Motor de arranque estándar."),
    ("Regulador Rectificador", "Eléctrico", "OEM", 75000, 6, "Regulador de voltaje de 12V."),
    ("Pito / Bocina 12V", "Eléctrico", "Genérico", 15000, 15, "Bocina estándar tipo caracol."),
    ("Fusibles Muela (Set x10)", "Eléctrico", "Genérico", 10000, 30, "Set de fusibles de 10A, 15A y 20A."),

    # 🌬️ FILTROS (10)
    ("Filtro de Aceite de Papel", "Filtros", "K&N", 35000, 15, "Filtro de alto flujo KN."),
    ("Filtro de Aceite Metálico", "Filtros", "OEM", 15000, 30, "Filtro de aceite estándar interno."),
    ("Filtro de Aire Original", "Filtros", "OEM Yamaha", 45000, 10, "Elemento filtrante de aire."),
    ("Filtro de Aire Alto Flujo", "Filtros", "K&N", 120000, 4, "Filtro lavable de larga duración."),
    ("Filtro de Aire Deportivo", "Filtros", "DNA", 150000, 3, "Filtro de aire deportivo de alto flujo."),
    ("Filtro de Gasolina en línea", "Filtros", "Genérico", 5000, 40, "Filtro de combustible transparente."),
    ("Filtro de Gasolina Metálico", "Filtros", "OEM", 12000, 15, "Filtro de combustible metálico reutilizable."),
    ("Filtro de Aire Esponja", "Filtros", "Twin Air", 65000, 6, "Filtro de espuma lavable para off-road."),
    ("Filtro de Aceite Suzuki", "Filtros", "OEM Suzuki", 20000, 10, "Filtro de aceite original Suzuki."),
    ("Filtro de Aire Honda", "Filtros", "OEM Honda", 40000, 8, "Filtro de aire original Honda."),

    # 🔩 MOTOR Y PARTES INTERNAS (18)
    ("Kit de Cilindro y Pistón STD", "Motor", "Vini", 180000, 3, "Cilindro completo con anillos y pasador."),
    ("Kit de Cilindro y Pistón 1er Over", "Motor", "Vini", 200000, 2, "Cilindro sobremedida 0.25mm."),
    ("Anillos de Pistón STD", "Motor", "NPR", 45000, 8, "Juego de anillos medida estándar."),
    ("Anillos de Pistón 1er Over", "Motor", "NPR", 48000, 6, "Anillos sobremedida 0.25mm."),
    ("Válvula de Admisión", "Motor", "OEM", 35000, 10, "Válvula original."),
    ("Válvula de Escape", "Motor", "OEM", 40000, 10, "Válvula original de escape."),
    ("Sellos de Válvula (Par)", "Motor", "NOK", 12000, 20, "Retenedores de aceite para válvulas."),
    ("Cadena de Distribución", "Motor", "DID", 55000, 8, "Cadenilla de tiempos."),
    ("Tensor de Cadenilla", "Motor", "OEM", 45000, 5, "Tensor automático de distribución."),
    ("Kit de Empaquetadura Motor", "Motor", "Vesrah", 65000, 6, "Juego completo de empaques para motor."),
    ("Empaque de Culata Metálica", "Motor", "OEM", 25000, 15, "Junta de culata metálica."),
    ("Discos de Clutch (Set)", "Motor", "FCC", 75000, 10, "Discos de embrague de fricción."),
    ("Separadores de Clutch", "Motor", "OEM", 40000, 6, "Platos metálicos separadores."),
    ("Rodamiento de Cigüeñal 6205", "Motor", "SKF", 28000, 12, "Balinera de alta revolución."),
    ("Rodamiento de Biela", "Motor", "NTN", 35000, 8, "Rodamiento de agujas para biela."),
    ("Pistón STD 53.5mm", "Motor", "Vertex", 65000, 6, "Pistón forjado medida estándar."),
    ("Pasador de Pistón", "Motor", "OEM", 15000, 15, "Pasador de acero cromado."),
    ("Kit de Resorte de Válvulas", "Motor", "OEM", 35000, 5, "Juego de resortes de válvula."),

    # 🛠️ SUSPENSIÓN Y DIRECCIÓN (12)
    ("Cunas de Dirección (Rodillos)", "Suspensión", "Triumph", 65000, 8, "Cunas cónicas para dirección suave."),
    ("Cunas de Dirección (Balines)", "Suspensión", "Genérico", 25000, 15, "Cunas estándar."),
    ("Retenedores de Suspensión (Par)", "Suspensión", "NOK", 35000, 12, "Retenedores de barras delanteras."),
    ("Guardapolvos de Suspensión", "Suspensión", "NOK", 25000, 10, "Protectores de barras."),
    ("Amortiguador Trasero Monoshock", "Suspensión", "YSS", 350000, 2, "Amortiguador de gas regulable."),
    ("Amortiguadores Traseros Dobles (Par)", "Suspensión", "OEM", 180000, 4, "Suspensión trasera estándar."),
    ("Horquilla Delantera Completa", "Suspensión", "OEM", 450000, 1, "Suspensión delantera completa con barras."),
    ("Barra de Horquilla (Una)", "Suspensión", "OEM", 120000, 3, "Barra cromada de suspensión delantera."),
    ("Resorte de Suspensión Delantera", "Suspensión", "Hyperpro", 180000, 2, "Resorte progresivo de alto rendimiento."),
    ("Fuelles de Suspensión (Par)", "Suspensión", "Genérico", 15000, 20, "Guardapolvos de caucho para barras."),
    ("Kit de Retenedores Horquilla", "Suspensión", "All Balls", 45000, 8, "Kit completo con retenedores y guardapolvos."),
    ("Buje de Suspensión Trasera", "Suspensión", "OEM", 25000, 10, "Buje de caucho para amortiguador."),

    # ⛓️ CABLES Y GUAYAS (10)
    ("Guaya de Acelerador", "Cables", "Control", 18000, 20, "Cable de acelerador lubricado."),
    ("Guaya de Clutch", "Cables", "Control", 20000, 25, "Cable de embrague alta resistencia."),
    ("Guaya de Choke (Estrangulador)", "Cables", "OEM", 15000, 10, "Cable para carburador."),
    ("Guaya de Freno Delantero", "Cables", "Genérico", 15000, 15, "Cable para freno delantero mecánico."),
    ("Guaya de Freno Trasero", "Cables", "Genérico", 15000, 15, "Cable para freno trasero mecánico."),
    ("Guaya de Velocímetro", "Cables", "Genérico", 12000, 15, "Cable para cuenta kilómetros."),
    ("Guaya de Apertura de Tanque", "Cables", "OEM", 12000, 10, "Cable de apertura de tapa de gasolina."),
    ("Kit de Guayas Completo", "Cables", "Control", 65000, 5, "Set de guayas principales para la moto."),
    ("Funda de Guaya (Metro)", "Cables", "Genérico", 5000, 30, "Funda plástica metrada para guayas."),
    ("Casquillo y Cono de Guaya", "Cables", "Genérico", 3000, 40, "Kit de ajuste para guayas."),

    # 🏍️ LLANTAS Y RUEDAS (12)
    ("Llanta Delantera 90/90-17", "Llantas", "Pirelli Diablo", 180000, 6, "Llanta pistera excelente agarre."),
    ("Llanta Trasera 130/70-17", "Llantas", "Michelin Pilot", 250000, 5, "Llanta radial duradera."),
    ("Llanta 110/70-17 Delantera", "Llantas", "Pirelli", 200000, 4, "Llanta deportiva delantera."),
    ("Llanta 150/60-17 Trasera", "Llantas", "Michelin", 280000, 3, "Llanta deportiva trasera."),
    ("Llanta Enduro 2.75-18", "Llantas", "Metzeler", 150000, 4, "Llanta doble propósito."),
    ("Llanta 90/90-18", "Llantas", "IRC", 140000, 5, "Llanta para motos de trabajo."),
    ("Neumático 17 (Cámara)", "Llantas", "IRC", 25000, 20, "Neumático estándar para llanta con radio."),
    ("Cámara de Aire 17x2.75", "Llantas", "Yokohama", 18000, 15, "Cámara de aire para llanta de radios."),
    ("Cámara de Aire 18x3.00", "Llantas", "Yokohama", 20000, 12, "Cámara de aire para llanta trasera."),
    ("Válvula Sellomatic", "Llantas", "Genérico", 8000, 30, "Válvula para llantas sin neumático."),
    ("Rodamiento Rueda Delantera 6202", "Ruedas", "SKF", 18000, 15, "Balinera sellada 6202."),
    ("Rodamiento Rueda Trasera 6302", "Ruedas", "SKF", 20000, 12, "Balinera sellada 6302."),
    ("Cauchos de Campana (Cush Drive)", "Ruedas", "OEM", 25000, 12, "Antivibrantes para la rueda trasera."),
    ("Eje de Rueda Delantera", "Ruedas", "OEM", 45000, 5, "Eje de acero para rueda delantera."),

    # 🚗 CARROCERÍA (15)
    ("Manigueta de Freno", "Carrocería", "OEM", 15000, 20, "Palanca de freno derecho."),
    ("Manigueta de Clutch", "Carrocería", "OEM", 15000, 20, "Palanca de embrague izquierdo."),
    ("Maniguetas Regulables (Par)", "Carrocería", "Racing", 85000, 5, "Maniguetas regulables de aluminio anodizado."),
    ("Cúpula / Visor Ahumado", "Carrocería", "Puig Replica", 75000, 4, "Visor aerodinámico ahumado."),
    ("Cúpula Transparente", "Carrocería", "Puig Replica", 70000, 4, "Visor aerodinámico transparente."),
    ("Guardabarros Delantero", "Carrocería", "OEM", 65000, 3, "Pieza plástica original."),
    ("Guardabarros Trasero", "Carrocería", "OEM", 55000, 3, "Guardabarros trasero completo."),
    ("Tapa Lateral (Par)", "Carrocería", "OEM", 45000, 4, "Tapas laterales de la moto."),
    ("Carenado Completo Delantero", "Carrocería", "OEM", 250000, 1, "Carenado frontal completo."),
    ("Estribo Izquierdo", "Carrocería", "OEM", 25000, 8, "Estribo completo con caucho."),
    ("Estribo Derecho", "Carrocería", "OEM", 25000, 8, "Estribo completo con caucho y pedal de freno."),
    ("Pedal de Freno Trasero", "Carrocería", "OEM", 35000, 6, "Pedal de freno trasero de acero."),
    ("Pedal de Arranque (Patada)", "Carrocería", "OEM", 28000, 5, "Pedal de arranque con retén."),
    ("Pata de Cabra (Side Stand)", "Carrocería", "OEM", 35000, 8, "Soporte lateral con resorte."),
    ("Pata Central (Center Stand)", "Carrocería", "OEM", 55000, 4, "Soporte central de acero."),

    # 🎯 ACCESORIOS (18)
    ("Espejos Retrovisores (Par)", "Accesorios", "Genérico", 35000, 10, "Espejos tipo originales."),
    ("Espejos Tipo Rizoma", "Accesorios", "Rizoma Replica", 55000, 8, "Espejos deportivos de aluminio."),
    ("Espejos Redondos Clásicos", "Accesorios", "Genérico", 25000, 12, "Espejos redondos estilo café racer."),
    ("Direccionales LED (Par)", "Accesorios", "LighTech", 45000, 12, "Indicadores LED secuenciales."),
    ("Direccionales Tipo Lápiz", "Accesorios", "Genérico", 25000, 15, "Direccionales LED delgadas."),
    ("Mangos / Grips Protaper", "Accesorios", "Protaper", 35000, 15, "Mangos de goma suave para manubrio."),
    ("Puños Calefactables", "Accesorios", "Oxford", 180000, 3, "Puños con calefacción integrada."),
    ("Protector de Tanque", "Accesorios", "Tankpad", 20000, 20, "Pad de resina para evitar rayones."),
    ("Tanque de Gasolina Universal", "Accesorios", "OEM", 280000, 2, "Tanque de gasolina estándar."),
    ("Tapa de Tanque", "Accesorios", "OEM", 35000, 10, "Tapa de gasolina con llave."),
    ("Portaplaca Metálico", "Accesorios", "Genérico", 15000, 25, "Soporte para placa estándar."),
    ("Sliders / Topes Anticaída", "Accesorios", "FireParts", 120000, 5, "Protectores de motor laterales."),
    ("Defensa de Motor Tubular", "Accesorios", "Promoto", 95000, 4, "Defensa metálica tubular."),
    ("Alarma para Moto", "Accesorios", "Genérico", 45000, 6, "Alarma con control remoto."),
    ("GPS Tracker", "Accesorios", "Conet", 120000, 4, "Rastreador GPS para moto."),
    ("Soporte para Celular", "Accesorios", "SP Connect", 85000, 5, "Soporte de manubrio para smartphone."),
    ("Cargador USB 12V", "Accesorios", "Genérico", 25000, 15, "Cargador USB para moto."),
    ("Cable de Carga para Batería", "Accesorios", "Genérico", 15000, 20, "Cargador de batería inteligente."),

    # 🧪 QUÍMICOS Y LIMPIEZA (12)
    ("Limpiador de Carburador", "Químicos", "Simoniz", 18000, 20, "Spray CarbuClean."),
    ("Desengrasante Industrial Galón", "Químicos", "Binner", 25000, 10, "Galón de desengrasante para motor."),
    ("Silicona Alta Temperatura", "Químicos", "Loctite", 15000, 15, "Formador de empaques gris."),
    ("Traba Roscas Azul", "Químicos", "Loctite 242", 28000, 5, "Pegante de tornillos resistencia media."),
    ("Traba Roscas Rojo", "Químicos", "Loctite 262", 30000, 5, "Pegante de tornillos alta resistencia."),
    ("Soldadura en Frío", "Químicos", "Devcon", 35000, 6, "Resina epóxica metálica."),
    ("Silicona Restauradora Plásticos", "Químicos", "Meguiars", 45000, 6, "Restaurador de plásticos."),
    ("Champú para Moto", "Químicos", "Simoniz", 15000, 20, "Jabón con cera carnauba."),
    ("Cera en Spray", "Químicos", "Meguiars", 35000, 8, "Cera líquida de alto brillo."),
    ("Limpiador de Cadenas C1", "Químicos", "Motul", 35000, 15, "Spray desengrasante para cadenas."),
    ("Pulidor de Metales", "Químicos", "Autosol", 25000, 12, "Pasta pulidora para cromo y acero."),
    ("Limpiador de Inyectores", "Químicos", "STP", 28000, 10, "Aditivo limpiador para combustible."),

    # ⛽ COMBUSTIBLE Y CARBURACIÓN (10)
    ("Kit de Carburador Completo", "Combustible", "Keyster", 45000, 8, "Punzón, chicleres y empaques."),
    ("Chicler de Alta 110", "Combustible", "OEM", 8000, 30, "Boquerel principal."),
    ("Chicler de Baja 30", "Combustible", "OEM", 8000, 30, "Boquerel de mínima."),
    ("Manguera de Gasolina 1/4 (metro)", "Combustible", "Genérico", 5000, 40, "Metro de manguera resistente a hidrocarburos."),
    ("Llave de Paso de Gasolina", "Combustible", "OEM", 25000, 10, "Grifo de combustible del tanque."),
    ("Tanque de Reserva 5L", "Combustible", "Genérico", 35000, 8, "Tanque auxiliar de gasolina."),
    ("Cinta de Tanque (Par)", "Combustible", "OEM", 18000, 10, "Bandas elásticas para sujetar tanque."),
    ("Inyector de Combustible", "Combustible", "OEM", 120000, 3, "Inyector electrónico de combustible."),
    ("Bomba de Gasolina Eléctrica", "Combustible", "OEM", 95000, 4, "Bomba de combustible sumergible."),
    ("Flotador de Tanque", "Combustible", "OEM", 25000, 10, "Medidor de gasolina."),

    # 🌡️ REFRIGERACIÓN (8)
    ("Refrigerante Anticongelante", "Fluidos", "Motul", 28000, 20, "Motocool Expert, protege el sistema de refrigeración."),
    ("Refrigerante Concentrado", "Fluidos", "Castrol", 35000, 10, "Anticongelante concentrado para mezclar."),
    ("Líquido Refrigerante Premezclado", "Fluidos", "OEM", 25000, 15, "Refrigerante listo para usar."),
    ("Radiador de Enfriamiento", "Fluidos", "OEM", 250000, 2, "Radiador de agua completo."),
    ("Tapa de Radiador", "Fluidos", "OEM", 12000, 20, "Tapa de presión para radiador."),
    ("Ventilador Eléctrico", "Fluidos", "OEM", 75000, 4, "Ventilador de radiador 12V."),
    ("Manguera de Radiador Superior", "Fluidos", "OEM", 25000, 8, "Manguera de caucho reforzado."),
    ("Termostato", "Fluidos", "OEM", 28000, 8, "Válvula termostática del motor."),

    # 🔊 SISTEMA DE ESCAPE (8)
    ("Tubo de Escape Completo", "Escape", "OEM", 250000, 2, "Sistema de escape completo original."),
    ("Silenciador Deportivo", "Escape", "Akrapovic Replica", 350000, 2, "Silenciador de alto flujo."),
    ("Empaque de Escape", "Escape", "OEM", 8000, 25, "Junta de múltiple de escape."),
    ("Abrazadera de Escape 1.5", "Escape", "Genérico", 5000, 30, "Abrazadera metálica para tubo."),
    ("Kit de Junta de Escape", "Escape", "OEM", 15000, 15, "Juego de juntas para sistema escape."),
    ("Decibelímetro / Reductor de Ruido", "Escape", "Genérico", 25000, 8, "Reductor de sonido para escape deportivo."),
    ("Cubre Cilindros (Múltiple)", "Escape", "OEM", 45000, 5, "Protector térmico de múltiple de escape."),
    ("Catalizador Universal", "Escape", "Genérico", 85000, 3, "Conversor catalítico universal."),

    # 🧰 HERRAMIENTAS Y TALLER (8)
    ("Kit de Herramientas para Moto", "Herramientas", "Genérico", 55000, 10, "Set básico con llaves y dados."),
    ("Crique de Horquilla Elevador", "Herramientas", "FireParts", 180000, 3, "Crique de piso para moto."),
    ("Soporte de Basculante (Padock)", "Herramientas", "Genérico", 45000, 6, "Soporte trasero para mantenimiento."),
    ("Llave de Bujía Magnética", "Herramientas", "Genérico", 12000, 20, "Llave de bujía imantada 5/8."),
    ("Compresor de Resorte de Suspensión", "Herramientas", "Genérico", 25000, 8, "Herramienta para desmontar horquilla."),
    ("Calibrador de Prensa", "Herramientas", "Genérico", 15000, 12, "Compresor de resortes de válvula."),
    ("Embudo para Aceite", "Herramientas", "Genérico", 8000, 30, "Embudo plástico con manguera."),
    ("Medidor de Batería", "Herramientas", "Genérico", 35000, 8, "Multímetro digital básico."),

    # 🏁 VARIOS / OTROS (8)
    ("Insumos Menores de Taller", "Otros", "Varios", 5000, 100, "Cobro por wipe, amarres, limpiador, etc."),
    ("Amarres Plásticos (Bolsa x50)", "Otros", "Genérico", 8000, 25, "Cintas de amarre de nylon."),
    ("Cinta Aislante Negra", "Otros", "3M", 5000, 30, "Rollo de cinta aislante."),
    ("Cinta Doble Faz", "Otros", "3M", 12000, 20, "Cinta adhesiva espumada de doble cara."),
    ("Trapo Industrial (Bolsa 5kg)", "Otros", "Genérico", 15000, 15, "Trapo absorbente para taller."),
    ("Guantes de Nitrilo (Caja x100)", "Otros", "Genérico", 35000, 8, "Guantes desechables para taller."),
    ("Bolsas para Repuestos", "Otros", "Genérico", 2000, 100, "Bolsa plástica sellable."),
    ("Stickers Multimarcas Brazo", "Otros", "Multimarcas", 5000, 50, "Pack de stickers del taller."),
]

with app.app_context():
    agregados = 0
    for nombre, cat, marca, precio, stock, desc in repuestos_data:
        existe = Repuesto.query.filter_by(nombre=nombre).first()
        if not existe:
            nuevo = Repuesto(
                nombre=nombre,
                categoria=cat,
                marca=marca,
                precio=precio,
                stock=stock,
                descripcion=desc
            )
            db.session.add(nuevo)
            agregados += 1

    db.session.commit()
    print(f"[OK] Se agregaron {agregados} repuestos nuevos.")
    print(f"Total en inventario: {Repuesto.query.count()} repuestos.")
