##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class PyPsutil(PythonPackage):
    """psutil is a cross-platform library for retrieving information on
    running processes and system utilization (CPU, memory, disks, network)
    in Python."""

    homepage = "https://pypi.python.org/pypi/psutil"
    url      = "https://pypi.python.org/packages/d9/c8/8c7a2ab8ec108ba9ab9a4762c5a0d67c283d41b13b5ce46be81fdcae3656/psutil-5.0.1.tar.gz"

    version('5.0.1', '153dc8be94badc4072016ceeac7808dc')

    depends_on('python@2.6:')
    depends_on('py-setuptools', type='build')
