%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           openstack-magnetodb
Version:        0.0.1
Release:        13%{?dist}
Group:          Development/Libraries
License:        Apache 2.0
Source0:        magnetodb-%{version}.tar.gz
Source1:        openstack-magnetodb-api
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:  python-devel, python-setuptools,
Provides:       %{name} = %{version}-%{release}
Summary:        openstack-magnetodb
BuildArch:      noarch
Requires:       python-cassandradriver >= 1.0.0b7
Requires:       python-eventlet >= 0.13
Requires:       python-iso8601 >= 0.1.4
Requires:       python-jsonschema >= 1.3.0, python-jsonschema <= 1.4.0
Requires:       python-kombu >= 2.4.8
Requires:       python-oslo-config >= 1.2.0
Requires:       python-pbr >= 0.5.21, python-pbr < 1.0
Requires:       python-keystoneclient >= 0.3.2
Requires:       python-babel >= 0.9.6
Requires:       python-paste-deploy = 1.5.0
Requires:       python-routes >= 1.12.3
Requires:       python-webob >= 1.2.3, python-webob < 1.3
Requires:       python27 = 2.7.1
Requires:       python27-tools = 2.7.1


%define debug_package %{nil}

%description
openstack-magnetodb

%prep
%setup -q -n magnetodb-%{version}



%build
%{__python} setup.py  build


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1  --root %{buildroot}

mkdir -p %{buildroot}/var/log/magnetodb
mkdir -p %{buildroot}/var/run/magnetodb
mkdir -p %{buildroot}/etc/magnetodb/
mkdir -p %{buildroot}/etc/init.d

install -p -D -m 755 %{SOURCE1}  %{buildroot}%{_initrddir}/openstack-magnetodb-api

cp %{_builddir}/magnetodb-%{version}/etc/* %{buildroot}%{_sysconfdir}/magnetodb/

chmod +x  %{buildroot}/usr/bin/*
chmod +x  %{buildroot}%{_initrddir}/openstack-magnetodb-api

sed -i s#'/usr/bin/env python'#'/usr/bin/env python27'#g %{buildroot}%{_bindir}/magnetodb-api-server
sed -i s#'/usr/bin/python'#'/usr/bin/python27'#g %{buildroot}%{_bindir}/magnetodb-api-server


%clean
rm -rf %{buildroot}


%files
#%defattr(644,root,root,755)
#%{python_sitelib}/*
/usr/*
%{python_sitelib}/
%{_bindir}/
%dir /var/log/magnetodb
%dir /var/run/magnetodb
%dir %{_sysconfdir}/magnetodb
%config(noreplace) %attr(-, root, root) %{_sysconfdir}/magnetodb/*
%config(noreplace) %attr(-, root, root) %{_initrddir}/openstack-magnetodb-api


%changelog
* Sun Dec 13 2013 Max Mazur <mmaxur@mirantis.com>
 - For Havanna  (fuel 4.0)
















