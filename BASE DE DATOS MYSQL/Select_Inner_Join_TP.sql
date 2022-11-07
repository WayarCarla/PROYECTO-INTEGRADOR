-- LISTADO DE TODAS LAS PROPIEDADES --
select pr.Id_Propiedad, pr.Direccion_Propiedad, pr.Localidad, pr.Provincia, ti.Nombre_Tipo from db_inm_brf.`Propiedad` as pr  
inner join db_inm_brf.`tipo` as ti
on  pr.Id_Tipo = ti.Id_Tipo  
order by pr.Id_Propiedad; 


-- DISPONIBLES PARA VENTA --
select pr.Id_Propiedad, pr.Direccion_Propiedad, es.Nombre_Estado, op.Nombre_Operatoria_Comercial from db_inm_brf.`Propiedad` as pr  
inner join db_inm_brf.`Estado` as es
on  pr.Id_Estado = es.Id_Estado  
inner join db_inm_brf.`operatoria comercial` as op
on pr.Id_Operacion_Comercial = op.Id_Operatoria_Comercial
where op.Id_Operatoria_Comercial = 1 and es.Id_Estado = 1
order by pr.Id_Propiedad; 

-- DISPONIBLES PARA ALQUILER --
select pr.Id_Propiedad, pr.Direccion_Propiedad, es.Nombre_Estado, op.Nombre_Operatoria_Comercial from db_inm_brf.`Propiedad` as pr  
inner join db_inm_brf.`Estado` as es
on  pr.Id_Estado = es.Id_Estado  
inner join db_inm_brf.`operatoria comercial` as op
on pr.Id_Operacion_Comercial = op.Id_Operatoria_Comercial
where op.Id_Operatoria_Comercial = 2 and es.Id_Estado = 1
order by pr.Id_Propiedad; 

-- VENDIDAS --
select pr.Id_Propiedad, pr.Direccion_Propiedad, es.Nombre_Estado, op.Nombre_Operatoria_Comercial from db_inm_brf.`Propiedad` as pr  
inner join db_inm_brf.`Estado` as es
on  pr.Id_Estado = es.Id_Estado  
inner join db_inm_brf.`operatoria comercial` as op
on pr.Id_Operacion_Comercial = op.Id_Operatoria_Comercial
where op.Id_Operatoria_Comercial = 1 and es.Id_Estado = 2
order by pr.Id_Propiedad; 

-- ALQUILADAS --
select pr.Id_Propiedad, pr.Direccion_Propiedad, es.Nombre_Estado, op.Nombre_Operatoria_Comercial from db_inm_brf.`Propiedad` as pr  
inner join db_inm_brf.`Estado` as es
on  pr.Id_Estado = es.Id_Estado  
inner join db_inm_brf.`operatoria comercial` as op
on pr.Id_Operacion_Comercial = op.Id_Operatoria_Comercial
where op.Id_Operatoria_Comercial = 2 and es.Id_Estado = 2
order by pr.Id_Propiedad; 

-- SELECT CON INNER JOIN  MUESTRA TODOS LOS ATRIBUTOS DE LAS 3 TABLAS --
select * from db_inm_brf.`Propiedad` as pr  
inner join db_inm_brf.`Estado` as es
on pr.Id_Estado = es.Id_Estado
inner join db_inm_brf.`operatoria comercial` as op
on pr.Id_Operacion_Comercial = op.Id_Operatoria_Comercial; 

-- SELECCIONO 3 ATRIBUTOS --
select pr.Id_Propiedad, pr.Direccion_Propiedad, es.Nombre_Estado from db_inm_brf.`Propiedad` as pr  
inner join db_inm_brf.`Estado` as es
on  pr.Id_Estado = es.Id_Estado;  

-- SELECCIOO 4 ATRIBUTOS DE 3 TABLAS --
select pr.Id_Propiedad, pr.Direccion_Propiedad, es.Nombre_Estado, op.Nombre_Operatoria_Comercial from db_inm_brf.`Propiedad` as pr  
inner join db_inm_brf.`Estado` as es
on  pr.Id_Estado = es.Id_Estado  
inner join db_inm_brf.`operatoria comercial` as op
on pr.Id_Operacion_Comercial = op.Id_Operatoria_Comercial
order by pr.Id_Propiedad; 


