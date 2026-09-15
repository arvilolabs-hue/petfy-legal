"""Author-controlled EN/ES copy for the static Petfy site.

Legal pages are review drafts. Do not present them as effective policy without
resolving RELEASE_DECISIONS.md and updating the release status in build_site.py.
"""

PAGES = {
    "privacy": {
        "file": "privacy.html",
        "title": {"es": "Privacidad en Petfy", "en": "Privacy at Petfy"},
        "summary": {
            "es": "Qué información usamos, para qué sirve y cómo puedes decidir sobre tus datos.",
            "en": "What information we use, why we use it, and how you can make choices about your data.",
        },
        "sections": [
            (
                "responsable",
                {"es": "Quién ofrece Petfy", "en": "Who offers Petfy"},
                {
                    "es": "<p>Petfy se ofrece bajo la marca <strong>Arvilo Labs</strong>. Su titular y responsable del tratamiento de datos es <strong>Brandon Stevens Aragón Mejía</strong>, establecido en Managua, Nicaragua.</p><p>Para consultas de privacidad, soporte o eliminación de cuenta, escribe a <a href='mailto:arvilolabs@gmail.com'>arvilolabs@gmail.com</a>. Esta página cubre Petfy para iPhone y iPad y este sitio público.</p>",
                    "en": "<p>Petfy is offered under the <strong>Arvilo Labs</strong> brand. Its owner and data controller is <strong>Brandon Stevens Aragón Mejía</strong>, established in Managua, Nicaragua.</p><p>For privacy, support, or account-deletion questions, email <a href='mailto:arvilolabs@gmail.com'>arvilolabs@gmail.com</a>. This page covers Petfy for iPhone and iPad and this public site.</p>",
                },
            ),
            (
                "datos",
                {"es": "Datos que utilizamos", "en": "Information we use"},
                {
                    "es": "<p>Según las funciones que elijas, podemos tratar:</p><ul><li><strong>Cuenta y perfil:</strong> correo, proveedor de acceso, nombre, foto, idioma, ciudad y preferencias.</li><li><strong>Mascotas y cuidados:</strong> perfiles, fotos, peso, alimentación, vacunas, medicamentos, citas, síntomas, notas y recordatorios.</li><li><strong>IA:</strong> tus mensajes, respuestas, mascota y contexto de cuidados que selecciones, eventos de consentimiento y reportes.</li><li><strong>Ubicación:</strong> coordenadas en primer plano cuando solicitas veterinarias cercanas; ciudad o país si los guardas en tu perfil.</li><li><strong>Dispositivo y compras:</strong> identificadores de instalación, tokens de notificación, versión de la app, producto, estado de Premium y referencias de transacción.</li><li><strong>Soporte y seguridad:</strong> mensajes de ayuda, eventos de sesión y errores filtrados para proteger y mantener el servicio.</li></ul><p>Petfy no solicita directamente números de tarjeta, documentos oficiales, contactos, grabaciones de micrófono ni ubicación continua en segundo plano en la versión actual. Apple gestiona el cobro de App Store.</p>",
                    "en": "<p>Depending on the features you choose, we may process:</p><ul><li><strong>Account and profile:</strong> email, sign-in provider, name, photo, language, city, and preferences.</li><li><strong>Pets and care:</strong> profiles, photos, weight, feeding, vaccines, medicines, appointments, symptoms, notes, and reminders.</li><li><strong>AI:</strong> your messages, responses, the pet and care context you select, consent events, and reports.</li><li><strong>Location:</strong> foreground coordinates when you request nearby vets; city or country if you save them to your profile.</li><li><strong>Device and purchases:</strong> installation identifiers, notification tokens, app version, product, Premium status, and transaction references.</li><li><strong>Support and security:</strong> help messages, session events, and filtered errors used to protect and maintain the service.</li></ul><p>The current Petfy app does not directly request payment-card numbers, government IDs, contacts, microphone recordings, or continuous background location. Apple handles App Store billing.</p>",
                },
            ),
            (
                "finalidades",
                {"es": "Para qué los usamos", "en": "Why we use it"},
                {
                    "es": "<p>Usamos esta información para crear y proteger tu cuenta, mostrar y sincronizar los registros de cuidado que introduces, enviar recordatorios, buscar veterinarias cuando lo pides, responder en Petfy AI después de tu consentimiento, comprobar Premium, atender soporte y mantener la seguridad y estabilidad de la app.</p><p>La base jurídica concreta para cada finalidad y país debe aprobarse antes de publicar una política definitiva; este borrador no presenta ese análisis como resuelto.</p>",
                    "en": "<p>We use this information to create and protect your account, display and sync the care records you enter, send reminders, look up vets when you ask, answer through Petfy AI after your consent, check Premium access, handle support, and maintain app security and reliability.</p><p>The specific lawful basis for each purpose and country must be approved before a final policy is published; this draft does not present that analysis as complete.</p>",
                },
            ),
            (
                "opciones",
                {"es": "Tus permisos y opciones", "en": "Your permissions and choices"},
                {
                    "es": "<p>La ubicación, el acceso a fotos y las notificaciones son opcionales. Puedes rechazarlos o revocarlos en los ajustes de iOS; las funciones que los necesitan dejarán de estar disponibles. Las búsquedas de veterinarias usan ubicación solo mientras realizas la búsqueda y Petfy no crea un historial de coordenadas.</p><p>Petfy AI requiere consentimiento dentro de la app. Puedes retirarlo y eliminar conversaciones guardadas desde los controles de IA.</p>",
                    "en": "<p>Location, photo access, and notifications are optional. You can decline or revoke them in iOS settings; features that need them will stop working. Vet searches use location only while you make the request, and Petfy does not create a coordinate history.</p><p>Petfy AI requires in-app consent. You can withdraw it and delete saved conversations through the AI controls.</p>",
                },
            ),
            (
                "proveedores",
                {"es": "Servicios que participan", "en": "Services involved"},
                {
                    "es": "<p>Para prestar las funciones usamos <strong>Supabase</strong> (cuentas, base de datos y archivos), <strong>OpenAI</strong> (respuestas de IA con el contexto elegido), <strong>Google Places/Maps</strong> (búsqueda de veterinarias), <strong>RevenueCat</strong> (estado de suscripción), <strong>Sentry</strong> (diagnósticos filtrados), <strong>Expo Push Service</strong> y <strong>Apple APNs</strong> (notificaciones). Apple también interviene en el inicio de sesión con Apple, distribución y compras.</p><p>Supabase está alojado para este proyecto en Estados Unidos, región East US. Otros servicios pueden tratar información fuera de tu país. Los mecanismos jurídicos de transferencia y los plazos contractuales siguen pendientes de verificación.</p>",
                    "en": "<p>To provide features, we use <strong>Supabase</strong> (accounts, database, and files), <strong>OpenAI</strong> (AI responses with selected context), <strong>Google Places/Maps</strong> (vet searches), <strong>RevenueCat</strong> (subscription state), <strong>Sentry</strong> (filtered diagnostics), <strong>Expo Push Service</strong>, and <strong>Apple APNs</strong> (notifications). Apple also handles Sign in with Apple, distribution, and purchases.</p><p>Supabase for this project is hosted in East US. Other services may process information outside your country. Legal transfer mechanisms and contractual retention periods remain to be verified.</p>",
                },
            ),
            (
                "conservacion",
                {"es": "Conservación y eliminación", "en": "Retention and deletion"},
                {
                    "es": "<p>Los datos de cuenta y de cuidado se conservan mientras la cuenta o el registro correspondiente exista, salvo que deban conservarse ciertos registros por obligaciones legales o disputas. Puedes borrar registros y conversaciones desde la app y solicitar la <a href='delete-account.html'>eliminación de tu cuenta</a>.</p><p>Los períodos o criterios específicos para copias de seguridad, diagnósticos, eventos de seguridad y consentimiento, soporte y transacciones necesitan aprobación. Este borrador no promete un borrado inmediato en todos los sistemas de proveedores.</p>",
                    "en": "<p>Account and care data remain while the account or relevant record exists, except for limited records that may need to be kept for legal obligations or disputes. You can delete records and conversations in the app and request <a href='delete-account.html'>account deletion</a>.</p><p>Specific periods or criteria for backups, diagnostics, security and consent events, support, and transactions require approval. This draft does not promise immediate deletion in every provider system.</p>",
                },
            ),
            (
                "derechos",
                {"es": "Tus derechos y seguridad", "en": "Your rights and security"},
                {
                    "es": "<p>Según tu país, puedes solicitar acceso, corrección, exportación, eliminación, limitación u oposición al tratamiento y retirar un consentimiento otorgado. Escríbenos desde el correo vinculado a tu cuenta a <a href='mailto:arvilolabs@gmail.com?subject=Petfy%20-%20Privacidad'>arvilolabs@gmail.com</a>. Podemos pedir verificación proporcional antes de actuar sobre datos de una cuenta.</p><p>Petfy usa acceso autenticado, reglas de propiedad sobre los datos y archivos privados. Filtra diagnósticos para reducir datos personales enviados a Sentry. Ningún servicio puede garantizar seguridad absoluta.</p>",
                    "en": "<p>Depending on your country, you may request access, correction, export, deletion, restriction, or objection, and withdraw consent you have given. Email us from the address linked to your account at <a href='mailto:arvilolabs@gmail.com?subject=Petfy%20-%20Privacy'>arvilolabs@gmail.com</a>. We may request proportionate verification before acting on account data.</p><p>Petfy uses authenticated access, ownership rules for data, and private files. It filters diagnostics to reduce personal information sent to Sentry. No service can guarantee absolute security.</p>",
                },
            ),
            (
                "menores",
                {"es": "Uso por menores", "en": "Use by minors"},
                {
                    "es": "<p>Petfy no establece una edad mínima adicional para todos los países. La disponibilidad para menores y las autorizaciones exigidas dependen de la ley aplicable y de las funciones utilizadas. Antes del lanzamiento internacional, debe revisarse la protección de menores por mercado; este borrador no afirma que la app tenga ya un mecanismo de consentimiento parental.</p>",
                    "en": "<p>Petfy does not set an additional worldwide minimum age. Availability for minors and required authorizations depend on local law and the features used. Child protection must be reviewed by market before international launch; this draft does not claim the app already has a parental-consent mechanism.</p>",
                },
            ),
            (
                "cambios",
                {"es": "Cambios y contacto", "en": "Changes and contact"},
                {
                    "es": "<p>Publicaremos una nueva fecha y versión cuando cambie una política aprobada. Si el cambio necesita una comunicación o consentimiento adicional, lo gestionaremos antes de aplicarlo. Consultas: <a href='mailto:arvilolabs@gmail.com'>arvilolabs@gmail.com</a>.</p>",
                    "en": "<p>We will publish a new date and version when an approved policy changes. If a change requires additional notice or consent, we will handle that before it takes effect. Questions: <a href='mailto:arvilolabs@gmail.com'>arvilolabs@gmail.com</a>.</p>",
                },
            ),
        ],
    },
    "terms": {
        "file": "terms.html",
        "title": {"es": "Condiciones de uso", "en": "Terms of use"},
        "summary": {
            "es": "Reglas claras para usar Petfy, Premium y las funciones de ayuda para tu mascota.",
            "en": "Clear rules for using Petfy, Premium, and features that help with your pet.",
        },
        "sections": [
            ("servicio", {"es": "Petfy y tu cuenta", "en": "Petfy and your account"}, {"es": "<p>Petfy es operada por <strong>Brandon Stevens Aragón Mejía</strong> en Managua, Nicaragua, bajo la marca <strong>Arvilo Labs</strong>. Permite organizar mascotas, cuidados, recordatorios, fotos, reportes, veterinarias cercanas y funciones opcionales de IA. Debes mantener segura tu cuenta y proporcionar información que tengas derecho a utilizar.</p><p>Petfy no fija una edad mínima adicional a escala mundial. El uso por menores deberá cumplir las autorizaciones y reglas locales aplicables; este punto requiere revisión antes de hacer vigentes las condiciones.</p>", "en": "<p>Petfy is operated by <strong>Brandon Stevens Aragón Mejía</strong> in Managua, Nicaragua, under the <strong>Arvilo Labs</strong> brand. It helps organize pets, care records, reminders, photos, reports, nearby vets, and optional AI features. Keep your account secure and provide information you have the right to use.</p><p>Petfy does not set an additional worldwide minimum age. Use by minors must comply with applicable local rules and authorizations; this point needs review before these terms become effective.</p>"}),
            ("uso", {"es": "Uso responsable", "en": "Responsible use"}, {"es": "<p>No uses Petfy para infringir derechos de terceros, introducir contenido ilegal, eludir controles de acceso o compra, atacar el servicio, suplantar a otros ni perjudicar a personas o animales. Puedes eliminar tu cuenta desde la app.</p><p>Conservas los derechos sobre fotos y textos que aportas. Autorizas el tratamiento limitado necesario para almacenar, mostrar, sincronizar y proteger los contenidos de las funciones que solicitas.</p>", "en": "<p>Do not use Petfy to infringe others' rights, upload illegal material, bypass access or purchase controls, attack the service, impersonate others, or harm people or animals. You can delete your account in the app.</p><p>You retain rights to the photos and text you provide. You allow the limited processing needed to store, display, sync, and protect content for the features you request.</p>"}),
            ("premium", {"es": "Petfy Premium y compras", "en": "Petfy Premium and purchases"}, {"es": "<p>Petfy Premium ofrece opciones de suscripción semanal y anual con renovación automática mediante la App Store de Apple. El precio, moneda, impuestos, período y condiciones aplicables se muestran en la tienda antes de confirmar la compra. La suscripción se cobra a tu cuenta Apple y se renueva según sus reglas hasta que la canceles allí.</p><p>Puedes <a href='https://apps.apple.com/account/subscriptions'>administrar o cancelar suscripciones con Apple</a> y usar «Restaurar compras» en Petfy para recuperar acceso elegible. Desinstalar la app o eliminar tu cuenta Petfy <strong>no cancela</strong> una suscripción Apple. Las solicitudes de reembolso y los problemas de cobro se gestionan a través de Apple según sus reglas y la ley aplicable.</p>", "en": "<p>Petfy Premium offers weekly and annual auto-renewing subscriptions through Apple's App Store. The store shows the current price, currency, taxes, period, and applicable terms before you confirm. Billing goes to your Apple account and renews under its rules until you cancel there.</p><p>You can <a href='https://apps.apple.com/account/subscriptions'>manage or cancel subscriptions with Apple</a> and use “Restore purchases” in Petfy to recover eligible access. Uninstalling the app or deleting your Petfy account <strong>does not cancel</strong> an Apple subscription. Refund requests and billing issues go through Apple under its rules and applicable law.</p>"}),
            ("cuidados", {"es": "Cuidados, IA y terceros", "en": "Care, AI, and third parties"}, {"es": "<p>Petfy es una herramienta de organización e información. No diagnostica, receta ni sustituye a un veterinario. Verifica medicamentos, dosis, síntomas y decisiones clínicas con un profesional; busca atención urgente cuando sea necesario.</p><p>Petfy AI necesita consentimiento y puede responder de forma incorrecta o incompleta. Los resultados de veterinarias provienen de servicios externos y pueden cambiar; comprueba horarios, disponibilidad y ubicación con la clínica.</p>", "en": "<p>Petfy is an organization and information tool. It does not diagnose, prescribe, or replace a veterinarian. Check medicine, doses, symptoms, and clinical decisions with a professional; seek urgent care when needed.</p><p>Petfy AI requires consent and may give incomplete or wrong answers. Vet results come from external services and can change; confirm hours, availability, and location with the clinic.</p>"}),
            ("cambios", {"es": "Cambios, derechos y ayuda", "en": "Changes, rights, and help"}, {"es": "<p>Podemos modificar funciones por seguridad, requisitos de tienda, razones técnicas o mejoras del servicio. Los cambios materiales de condiciones tendrán nueva versión y fecha y se comunicarán cuando corresponda.</p><p>Nada en estas condiciones pretende excluir derechos del consumidor que la ley no permita excluir. La ley aplicable, jurisdicción y límites de responsabilidad necesitan revisión jurídica para los países de lanzamiento. Para ayuda, escribe a <a href='mailto:arvilolabs@gmail.com'>arvilolabs@gmail.com</a>.</p>", "en": "<p>We may change features for security, store requirements, technical reasons, or service improvements. Material changes to terms will have a new version and date and will be communicated where required.</p><p>These terms do not aim to exclude consumer rights that law does not permit us to exclude. Governing law, jurisdiction, and liability limits require legal review for launch countries. For help, email <a href='mailto:arvilolabs@gmail.com'>arvilolabs@gmail.com</a>.</p>"}),
        ],
    },
    "delete-account": {
        "file": "delete-account.html",
        "title": {"es": "Eliminar tu cuenta", "en": "Delete your account"},
        "summary": {"es": "Puedes iniciar el borrado desde Petfy o escribirnos si ya no puedes entrar.", "en": "You can start deletion in Petfy or email us if you can no longer sign in."},
        "sections": [
            ("app", {"es": "Desde la app", "en": "In the app"}, {"es": "<ol><li>Abre Petfy e inicia sesión en la cuenta correcta.</li><li>Entra en <strong>Más / Configuración</strong> y abre <strong>Seguridad</strong>.</li><li>Toca <strong>Eliminar cuenta y datos</strong>.</li><li>Lee la confirmación. Si Petfy lo solicita, vuelve a autenticarte con correo, Apple o Google y confirma.</li></ol><p>Esta opción elimina la cuenta completa, no solo la desactiva.</p>", "en": "<ol><li>Open Petfy and sign in to the account you want to delete.</li><li>Go to <strong>More / Settings</strong> and open <strong>Security</strong>.</li><li>Tap <strong>Delete account and data</strong>.</li><li>Read the confirmation. If Petfy asks, authenticate again with email, Apple, or Google and confirm.</li></ol><p>This option deletes the whole account, not just deactivates it.</p>"}),
            ("sin-acceso", {"es": "Si no puedes entrar", "en": "If you cannot sign in"}, {"es": "<p>Envía un correo desde la dirección asociada a tu cuenta a <a href='mailto:arvilolabs@gmail.com?subject=Eliminar%20cuenta%20Petfy'>arvilolabs@gmail.com</a> con el asunto «Eliminar cuenta Petfy». Te indicaremos un método de verificación antes de actuar. En el primer mensaje no adjuntes contraseña, datos de tarjeta ni documentos de identidad.</p><p>El tiempo de respuesta y de finalización debe confirmarse antes de publicar esta página como proceso definitivo.</p>", "en": "<p>Email us from the address associated with your account at <a href='mailto:arvilolabs@gmail.com?subject=Delete%20Petfy%20account'>arvilolabs@gmail.com</a> with the subject “Delete Petfy account.” We will provide a verification method before acting. Do not attach a password, payment-card details, or government ID to the first message.</p><p>The response and completion time must be confirmed before this page is published as the definitive process.</p>"}),
            ("alcance", {"es": "Qué se elimina", "en": "What is deleted"}, {"es": "<p>El proceso elimina tu usuario de Petfy, perfil, archivos privados vinculados y registros propios de mascotas, cuidados, recordatorios, favoritos, dispositivos, conversaciones de IA y proyecciones de acceso Premium. Algunos registros de transacción, seguridad, consentimiento o disputas podrían conservarse si una obligación legal exige ello y durante el plazo aprobado en la política final. Apple conserva por separado el historial que su propia ley o política le exige.</p>", "en": "<p>The process deletes your Petfy user, profile, linked private files, and account-owned pet, care, reminder, favorite, device, AI-conversation, and Premium-access records. Some transaction, security, consent, or dispute records might be retained where legally required for the period approved in the final policy. Apple separately retains any history required by its own law or policy.</p>"}),
            ("suscripcion", {"es": "Antes de borrar: cancela Premium", "en": "Before deletion: cancel Premium"}, {"es": "<p><strong>Borrar la cuenta o desinstalar Petfy no detiene el cobro de una suscripción Apple.</strong> Si tienes Premium con renovación automática, cancélalo antes desde <a href='https://apps.apple.com/account/subscriptions'>Suscripciones de Apple</a> o en iPhone/iPad: Ajustes → tu nombre → Suscripciones → Petfy. Apple gestiona las renovaciones y reembolsos.</p>", "en": "<p><strong>Deleting the account or uninstalling Petfy does not stop billing for an Apple subscription.</strong> If you have auto-renewing Premium, cancel it first through <a href='https://apps.apple.com/account/subscriptions'>Apple Subscriptions</a> or on iPhone/iPad: Settings → your name → Subscriptions → Petfy. Apple handles renewals and refunds.</p>"}),
        ],
    },
    "ai-notice": {
        "file": "ai-notice.html",
        "title": {"es": "Cómo funciona Petfy AI", "en": "How Petfy AI works"},
        "summary": {"es": "Una ayuda para organizar información, con consentimiento y límites claros.", "en": "A way to organize information, with clear consent and limitations."},
        "sections": [
            ("envio", {"es": "Qué se envía", "en": "What is sent"}, {"es": "<p>Cuando aceptas usar Petfy AI y haces una consulta, se envía tu mensaje y el contexto de la mascota y sus cuidados que selecciones a la función segura de Petfy y al proveedor OpenAI para producir una respuesta. La conversación y la respuesta pueden guardarse en tu cuenta para que las consultes después.</p><p>No compartas contraseñas, datos de tarjeta o documentos oficiales en tus preguntas.</p>", "en": "<p>When you consent to Petfy AI and ask a question, your message and the pet and care context you select are sent to Petfy's secured function and to OpenAI for a response. The conversation and response may be stored in your account so you can revisit them.</p><p>Do not include passwords, card details, or government IDs in prompts.</p>"}),
            ("control", {"es": "Tú tienes el control", "en": "You stay in control"}, {"es": "<p>La IA es opcional y exige consentimiento en la app. Puedes retirar ese consentimiento, borrar una conversación o borrar las conversaciones guardadas. Los registros necesarios para seguridad y prueba de consentimiento requieren una regla final de conservación.</p>", "en": "<p>AI is optional and requires in-app consent. You can withdraw it, delete one conversation, or delete saved conversations. Records needed for security and evidence of consent still require a final retention rule.</p>"}),
            ("limites", {"es": "No sustituye a un veterinario", "en": "It does not replace a veterinarian"}, {"es": "<p>La IA puede equivocarse, omitir información o ofrecer una respuesta inadecuada. No la uses para diagnóstico, dosis, urgencias o tratamiento. Si tu mascota presenta dificultad respiratoria, convulsiones, intoxicación, sangrado u otro síntoma grave, busca atención veterinaria inmediata.</p>", "en": "<p>AI may be wrong, omit information, or give an unsuitable answer. Do not use it for diagnosis, doses, emergencies, or treatment. If your pet has breathing difficulty, seizures, poisoning, bleeding, or another serious symptom, seek veterinary care immediately.</p>"}),
        ],
    },
    "dmca": {
        "file": "dmca.html",
        "title": {"es": "Derechos de autor", "en": "Copyright"},
        "summary": {"es": "Cómo avisarnos si crees que un contenido de Petfy infringe tus derechos.", "en": "How to tell us if you believe Petfy content infringes your rights."},
        "sections": [
            ("reporte", {"es": "Enviar un aviso", "en": "Send a notice"}, {"es": "<p>Escribe a <a href='mailto:arvilolabs@gmail.com?subject=Petfy%20-%20Derechos%20de%20autor'>arvilolabs@gmail.com</a> con tu nombre y contacto, la obra protegida, el contenido concreto y dónde aparece, y una explicación de por qué consideras que no está autorizado. No envíes documentos de identidad en el primer correo.</p>", "en": "<p>Email <a href='mailto:arvilolabs@gmail.com?subject=Petfy%20-%20Copyright'>arvilolabs@gmail.com</a> with your name and contact details, the protected work, the specific content and where it appears, and why you believe it is unauthorized. Do not send government IDs in the first email.</p>"}),
            ("respuesta", {"es": "Si se retiró por error", "en": "If removal was a mistake"}, {"es": "<p>Puedes responder al mismo correo con el contexto y la prueba que consideres pertinente. Evaluaremos el aviso y podremos pedir información adicional. Esta página es un canal de contacto general; no afirma que exista un agente DMCA registrado.</p>", "en": "<p>You can reply to the same address with relevant context and evidence. We will assess the notice and may request more information. This is a general contact channel; it does not claim that a registered DMCA agent exists.</p>"}),
        ],
    },
}
