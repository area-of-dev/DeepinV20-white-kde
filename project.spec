# Copyright 2020 Alex Woroschilow <alex.woroschilow@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2,
# or (at your option) any later version, as published by the Free
# Software Foundation
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details
#
# You should have received a copy of the GNU General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
Summary: DeepinV20-white KDE Theme
Name: DeepinV20-white
Version: 1.0
Release: %(date +"%Y%m%d%H%M")
Source0: %{name}-%{version}-%{release}.tar.gz
Group: Application/Web
License: GPL-2.0
BuildArch: noarch

%define DIR_AURORAE     /usr/share/aurorae/themes
%define DIR_SCHEMES     /usr/share/color-schemes
%define DIR_PLASMA      /usr/share/plasma/desktoptheme
%define DIR_LAYOUT      /usr/share/plasma/layout-templates
%define DIR_LOOKFEEL    /usr/share/plasma/look-and-feel
%define DIR_WALLPAPER   /usr/share/wallpapers
%define DIR_KVANTUM     /usr/share/Kvantum
%define DIR_SDDM        /usr/share/sddm/themes
%define DIR_ICONS       /usr/share/icons
%define DIR_THEMES      /usr/share/themes

%define _unpackaged_files_terminate_build 0

%description
DeepinV20-white kde is a light clean theme for KDE Plasma desktop.

%prep
%setup -q

%install
install -d $RPM_BUILD_ROOT%{DIR_AURORAE}
install -d $RPM_BUILD_ROOT%{DIR_SCHEMES}
install -d $RPM_BUILD_ROOT%{DIR_PLASMA}
install -d $RPM_BUILD_ROOT%{DIR_LAYOUT}
install -d $RPM_BUILD_ROOT%{DIR_LOOKFEEL}
install -d $RPM_BUILD_ROOT%{DIR_WALLPAPER}
install -d $RPM_BUILD_ROOT%{DIR_KVANTUM}
install -d $RPM_BUILD_ROOT%{DIR_SDDM}
install -d $RPM_BUILD_ROOT%{DIR_ICONS}
install -d $RPM_BUILD_ROOT%{DIR_THEMES}
install -d $RPM_BUILD_ROOT%{DIR_ICONS}/DeepinV20-white
install -d $RPM_BUILD_ROOT%{DIR_ICONS}/DeepinV20-white/cursors
install -d $RPM_BUILD_ROOT%{DIR_ICONS}/DeepinV20-dark
install -d $RPM_BUILD_ROOT%{DIR_ICONS}/DeepinV20-dark/cursors

cp --recursive ./src/aurorae/*                                  $RPM_BUILD_ROOT%{DIR_AURORAE}
cp --recursive ./src/color-schemes/*.colors                     $RPM_BUILD_ROOT%{DIR_SCHEMES}
cp --recursive ./src/plasma/desktoptheme/DeepinV20-*            $RPM_BUILD_ROOT%{DIR_PLASMA}
cp --recursive ./src/plasma/look-and-feel/*                     $RPM_BUILD_ROOT%{DIR_LOOKFEEL}
cp --recursive ./src/wallpaper/*                                $RPM_BUILD_ROOT%{DIR_WALLPAPER}
cp --recursive ./src/Kvantum/*                                  $RPM_BUILD_ROOT%{DIR_KVANTUM}
cp --recursive ./src/themes/DeepinV20-*                         $RPM_BUILD_ROOT%{DIR_THEMES}
cp --recursive ./src/sddm/DeepinV20-*                           $RPM_BUILD_ROOT%{DIR_SDDM}
cp --recursive ./src/icons/DeepinV20-white                      $RPM_BUILD_ROOT%{DIR_ICONS}

cp --recursive ./src/cursor/DeepinV20-white/dist/cursors/*      $RPM_BUILD_ROOT%{DIR_ICONS}/DeepinV20-white/cursors
cp --recursive ./src/cursor/DeepinV20-dark/dist/*               $RPM_BUILD_ROOT%{DIR_ICONS}/DeepinV20-dark

find $RPM_BUILD_ROOT%{DIR_ICONS} -name "*.py"   -exec rm -rf {} \;
find $RPM_BUILD_ROOT%{DIR_ICONS} -name ".git*"  -exec rm -rf {} \;

%files 
%defattr(644,root,root,755)
%dir %{DIR_AURORAE}
%dir %{DIR_SCHEMES}
%dir %{DIR_PLASMA}
%dir %{DIR_LAYOUT}
%dir %{DIR_LOOKFEEL}
%dir %{DIR_WALLPAPER}
%dir %{DIR_KVANTUM}
%dir %{DIR_SDDM}
%dir %{DIR_ICONS}
%dir %{DIR_THEMES}

%{DIR_AURORAE}/*
%{DIR_SCHEMES}/*
%{DIR_PLASMA}/*
%{DIR_LOOKFEEL}/*
%{DIR_WALLPAPER}/*
%{DIR_KVANTUM}/*
%{DIR_SDDM}/*
%{DIR_ICONS}/*
%{DIR_THEMES}/*

