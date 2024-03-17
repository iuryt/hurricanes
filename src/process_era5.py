import xarray as xr

ds = xr.open_dataset("../data/external/adaptor.mars.internal-1710529024.4713497-6175-11-ace94687-57b5-4fcc-9a47-c54e323e83c6.nc")

clim = ds.groupby("time.month").mean()
clim = clim.coarsen(longitude = 10, latitude = 10, boundary = "pad").mean()
clim = xr.concat([clim.interp(longitude = 0, method = "nearest", kwargs={"fill_value": "extrapolate"}), clim], "longitude")

clim.to_netcdf("../data/processed/era5_climatology.nc")

