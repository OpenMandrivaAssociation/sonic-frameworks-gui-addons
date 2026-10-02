%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname SonicFrameworksGuiAddons
%define devname %mklibname SonicFrameworksGuiAddons -d
#define git 20240217

Name: sonic-frameworks-gui-addons
Version: 6.28.0
Release: %{?git:0.%{git}.}2
URL: https://github.com/Sonic-DE/sonic-frameworks-gui-addons
Source0: %url/archive/%version/%name-%version.tar.gz
Summary: Utilities for graphical user interfaces
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DBUILD_WITH_QT6:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: python%{pyver}dist(build)
BuildRequires: pkgconfig(python3)
BuildRequires: cmake(Shiboken6)
BuildRequires: cmake(PySide6)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
# BuildRequires: cmake(PlasmaWaylandProtocols)
# BuildRequires: cmake(Qt6WaylandClient)
# BuildRequires: pkgconfig(wayland-client)
# BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(vulkan)
Requires: %{libname} = %{EVRD}
Conflicts: kf6-kguiaddons

# %patchlist
# kguiaddons-6.18-pyside-compile.patch

%description
Utilities for graphical user interfaces

%package -n sonic-geo-scheme-handler
Summary: Geo scheme handler for SonicDE
Group: System/Libraries

Conflicts: kde-geo-scheme-handler

%description -n sonic-geo-scheme-handler
%summary

%package -n %{libname}
Summary: Utilities for graphical user interfaces
Group: System/Libraries
Requires: %{name} = %{EVRD}
Requires: sonic-geo-scheme-handler = %{EVRD}
Conflicts: %{_lib}KF6GuiAddons

%description -n %{libname}
Utilities for graphical user interfaces

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Conflicts: %{_lib}KF6GuiAddons-devel

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Utilities for graphical user interfaces

%package -n python-sonic-gui-addons
Summary: Python bindings to SonicDE GUIAddons
Group: Development/Python
Requires: %{libname} = %{EVRD}

%description -n python-sonic-gui-addons
%summary

%install -a
rm -rf %{buildroot}/%{_libdir}/cmake
rm -rf %{buildroot}/%{_libdir}/pkgconfig

%files
%{_datadir}/qlogging-categories6/kguiaddons.*

%files -n sonic-geo-scheme-handler
%{_bindir}/kde-geo-uri-handler
%{_datadir}/applications/google-maps-geo-handler.desktop
%{_datadir}/applications/openstreetmap-geo-handler.desktop
#{_datadir}/applications/qwant-maps-geo-handler.desktop
%{_datadir}/applications/wheelmap-geo-handler.desktop

%files -n %{devname}
%{_includedir}/KF6/KGuiAddons

# pending rename
# %{_libdir}/cmake/KF6GuiAddons
# %{_libdir}/pkgconfig/KF6GuiAddons.pc

%files -n %{libname}
%{_libdir}/libKF6GuiAddons.so*
%{_qtdir}/qml/org/kde/guiaddons

%files -n python-sonic-gui-addons
%{_libdir}/python*/site-packages/KGuiAddons.cpython-*.so
