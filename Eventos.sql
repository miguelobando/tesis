/****** Eventos de seguridad  ******/
SELECT [IdEvento]
      ,[IdTipoActivoXIndicador]
      ,[IdActivo]
      ,[IdCategoriaActivo]
      ,[IdEstado]
      ,[IdReglaEvento]
      ,[FechaHoraEvento]   
      ,[FechaHoraBitacora]
      ,[FechaHoraNormalizacion]
      ,[FechaHoraModificacion]
      ,[FechaHoraLocalEvento]
      ,[FechaHoraLocalNormalizacion]
      ,[IdEventoPadre]
  FROM [netmatrix].[dbo].[Evento]
  WHERE [IdReglaEvento] = 4 OR
        [IdReglaEvento] = 7 OR
        [IdReglaEvento] = 22 OR
        [IdReglaEvento] = 23 OR
        [IdReglaEvento] = 24 OR
        [IdReglaEvento] = 25 OR
        [IdReglaEvento] = 26 OR
        [IdReglaEvento] = 1013 OR
        [IdReglaEvento] = 1014 OR
        [IdReglaEvento] = 1017 OR
        [IdReglaEvento] = 1018 OR
        [IdReglaEvento] = 1021 OR
        [IdReglaEvento] = 1023 OR
        [IdReglaEvento] = 1024 OR
        [IdReglaEvento] = 1026 OR
        [IdReglaEvento] = 1028
 

/************EVENTOS DE FALLAS ******/

SELECT [IdEvento]
      ,[IdTipoActivoXIndicador]
      ,[IdActivo]
      ,[IdCategoriaActivo]
      ,[IdEstado]
      ,[IdReglaEvento]
      ,[FechaHoraEvento]   
      ,[FechaHoraBitacora]
      ,[FechaHoraNormalizacion]
      ,[FechaHoraModificacion]
      ,[FechaHoraLocalEvento]
      ,[FechaHoraLocalNormalizacion]
      ,[IdEventoPadre]
  FROM [netmatrix].[dbo].[Evento]
  WHERE 
    [IdReglaEvento] = 9 OR
    [IdReglaEvento] = 13 OR
    [IdReglaEvento] = 14 OR
    [IdReglaEvento] = 16 OR
    [IdReglaEvento] = 18 OR
    [IdReglaEvento] = 19 OR
    [IdReglaEvento] = 20 OR
    [IdReglaEvento] = 21 OR
    [IdReglaEvento] = 27 OR
    [IdReglaEvento] = 28 OR
    [IdReglaEvento] = 39 OR
    [IdReglaEvento] = 80 OR
    [IdReglaEvento] = 81 OR
    [IdReglaEvento] = 82 OR
    [IdReglaEvento] = 83 OR
    [IdReglaEvento] = 86
